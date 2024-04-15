import tokenize_code_numbers
from functools import cmp_to_key


def get_tokens_for_linter(simple_tokens):
    res = []
    cur = []
    for i in range(len(simple_tokens)):
        if simple_tokens[i][0] == tokenize_code_numbers.NEXT_LINE_NUM:
            cur.append(simple_tokens[i])
            res.append(cur)
            cur = []
        else:
            cur.append(simple_tokens[i])
    return res


def check_begin_end(tokens):
    res = []
    cur_vloz = 0
    cur_num_str = 1
    for i in range(len(tokens)):
        is_begin = False
        ok = True
        for j in range(len(tokens[i])):
            if tokens[i][j][0] == tokenize_code_numbers.code_numbers['end'].value:
                cur_vloz -= 1
            if tokens[i][j][0] == tokenize_code_numbers.code_numbers['begin'].value:
                cur_vloz += 1
                is_begin = True
            if tokens[i][j][0] == tokenize_code_numbers.NEXT_LINE_NUM:
                cur_num_str += tokens[i][j][1]
        if tokens[i][0][0] != tokenize_code_numbers.NEXT_LINE_NUM:
            if tokens[i][0][0] == tokenize_code_numbers.SPACE_NUM:
                srav = cur_vloz
                if is_begin:
                    srav -= 1
                if tokens[i][0][1] != srav * 2:
                    ok = False
            elif cur_vloz != 0 and not is_begin:
                ok = False
            elif cur_vloz > 1:
                ok = False
        if not ok:
            res.append([cur_num_str - tokens[i][-1][1], 'неверное количество пробелов в начале строки'])
    return res


def check_blank_line_before_cycle_if(tokens):
    res = []
    check_params = [tokenize_code_numbers.code_numbers['for'].value, tokenize_code_numbers.code_numbers['For'].value,
                    tokenize_code_numbers.code_numbers['while'].value,
                    tokenize_code_numbers.code_numbers['While'].value,
                    tokenize_code_numbers.code_numbers['if'].value]
    cur_num_str = 1
    for i in range(len(tokens)):
        ok = True
        for j in range(len(tokens[i])):
            if tokens[i][j][0] == tokenize_code_numbers.NEXT_LINE_NUM:
                cur_num_str += tokens[i][j][1]
            if tokens[i][j][0] in check_params:
                if i == 0 or tokens[i - 1][-1][0] != tokenize_code_numbers.NEXT_LINE_NUM or tokens[i - 1][-1][1] != 2:
                    ok = False
        if not ok:
            res.append([cur_num_str - tokens[i][-1][1], 'неверное количество отступов перед условием/циклом'])
    return res


def comp(item1, item2):
    if item1[0] <= item2[0]:
        return -1
    return 1


def get_error_lines(tokens):
    res = check_begin_end(tokens)
    res2 = check_blank_line_before_cycle_if(tokens)
    for i in res2:
        res.append(i)
    res = sorted(res, key=cmp_to_key(comp))
    return res
