from Levenshtein import distance as lev
import os
import tokenize_code_numbers

special_words = tokenize_code_numbers.code_numbers
RESUL_FILE_PATH = 'D:/ANNA/USB/CodeCopiedChecker/result.txt'


def check_special_word(s):
    for i in special_words.keys():
        if s.startswith(i):
            counter = 1
            if len(i) == 1:
                s = s[1:]
                while s.startswith(i):
                    counter += 1
                    s = s[1:]
            return [special_words[i], counter, i * counter]
    return False


def check_spaces(s):
    if s[0] != ' ':
        return False
    counter = 0
    i = 0
    while s[i] == ' ':
        counter += 1
        i += 1
    return [tokenize_code_numbers.SPACE_NUM, counter, ' ' * counter]


def check_comment(s):
    if s[0] != '{':
        return False
    i = 0
    while s[i] != '}':
        i += 1
    return [tokenize_code_numbers.COMMENT_NUM, 1, s[:i + 1]]


def check_string_value(s):
    if s[0] != '\'':
        return False
    i = 0
    while s[i] != '\'':
        i += 1
    return [tokenize_code_numbers.STRING_VALUE_NUM, 1, s[:i + 1]]


def check_number(s):
    if s[0] not in '1234567890':
        return False
    cur_var = ''
    l = 0
    while l < len(s) and s[l] in '1234567890':
        cur_var += s[l]
        l += 1
    return [tokenize_code_numbers.NUMBER_NUM, len(cur_var), cur_var]


def get_value(s):
    val = ''
    i = 0
    while i < len(s) and s[i] != ' ' and s[i] not in special_words.keys():
        val += s[i]
        i += 1
    return [tokenize_code_numbers.VARIABLE_NUM, 1, s[:i]]


def check_new_string(s):
    if s[0] != '\n':
        return False
    i = 0
    counter = 0
    while i < len(s) and s[i] == '\n':
        counter += 1
        i += 1
    return [tokenize_code_numbers.NEXT_LINE_NUM, counter, '\n' * counter]


def get_tokens(code):
    tokens = []
    while code != '':
        cur = check_comment(code)
        if cur == False:
            cur = check_spaces(code)
            if cur == False:
                cur = check_new_string(code)
                if cur == False:
                    cur = check_special_word(code)
                    if cur == False:
                        cur = check_string_value(code)
                        if cur == False:
                            cur = check_number(code)
                            if cur == False:
                                cur = get_value(code)
        tokens.append(cur)
        code = code[len(tokens[-1][2]):]
    return tokens


def check_2_codes(full=True):
    i = 0
    j = 0
    flag = False
    while i < len(t1) and j < len(t2):
        while i < len(t1) and (t1[i][0] == tokenize_code_numbers.COMMENT_NUM or t1[i][
            0] == tokenize_code_numbers.SPACE_NUM or t1[i][
                                   0] == tokenize_code_numbers.STRING_VALUE_NUM or t1[i][
                                   0] == tokenize_code_numbers.NEXT_LINE_NUM):
            i += 1
        while j < len(t2) and (t2[j][0] == tokenize_code_numbers.COMMENT_NUM or t2[j][
            0] == tokenize_code_numbers.SPACE_NUM or t2[j][
                                   0] == tokenize_code_numbers.STRING_VALUE_NUM or t2[j][
                                   0] == tokenize_code_numbers.NEXT_LINE_NUM):
            j += 1
        if i < len(t1) and j < len(t2) and (t1[i][0] != t2[j][0] or t1[i][2] != t2[j][2]):
            if not full and t1[i][0] != t2[j][0] or full:
                flag = True
                break
        i += 1
        j += 1
    return not flag


directory = 'D:/ANNA/USB/CodeCopiedChecker/codes_test'
files = []
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        files.append(f)
if not os.path.exists(RESUL_FILE_PATH):
    with open(RESUL_FILE_PATH, 'w'): pass
res = ''
for f1 in range(0, len(files) - 1):
    for f2 in range(f1 + 1, len(files)):
        with open(files[f1], 'r', encoding="utf-8") as file:
            code1 = file.read()
        with open(files[f2], 'r', encoding="utf-8") as file:
            code2 = file.read()
        t1 = get_tokens(code1)
        t2 = get_tokens(code2)
        res += files[f1] + ' ' + files[f2] + ' '
        if check_2_codes():
            res += '100 %'
        elif check_2_codes(False):
            res += 'second level'
        else:
            dist1 = ''
            dist2 = ''
            for i in t1:
                dist1 += str(i[0]) + ' '
            for j in t2:
                dist2 += str(j[0]) + ' '
            res += str(lev(dist1, dist2))
        res += '\n'
with open(RESUL_FILE_PATH, 'w', encoding="utf-8") as file:
    file.write(res)
