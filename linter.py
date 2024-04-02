import tokenize_code_numbers


def get_tokens_for_linter(simple_tokens):
    res = []
    cur = []
    for i in range(len(simple_tokens)):
        if simple_tokens[i][0] == tokenize_code_numbers.NEXT_LINE_NUM:
            res.append(cur)
            cur = []
        else:
            cur.append(simple_tokens[i])
    return res


def get_error_lines(tokens):
    res = []
    cur_vloz = 0
    for i in range(len(tokens)):
        is_begin = False
        for j in range(len(tokens[i])):
            if tokens[i][j][0] == tokenize_code_numbers.code_numbers['end'].value:
                cur_vloz -= 1
                if cur_vloz < 0:
                    res.append([i + 1, 'лишний end'])
            if tokens[i][j][0] == tokenize_code_numbers.code_numbers['begin'].value:
                cur_vloz += 1
                is_begin = True
        if tokens[i][0][0] == tokenize_code_numbers.SPACE_NUM:
            srav = cur_vloz
            if is_begin:
                srav -= 1
            if tokens[i][0][1] != srav * 2:
                res.append([i + 1, 'неверное количество пробелов в начале строки'])
        elif cur_vloz != 0 and not is_begin:
            res.append([i + 1, 'неверное количество пробелов в начале строки'])

    if cur_vloz < 0:
        res.append([len(tokens), 'лишние end ' + (str(-cur_vloz))])
    if cur_vloz > 0:
        res.append([len(tokens), 'лишние begin ' + (str(cur_vloz))])
    return res
