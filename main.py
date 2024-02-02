import re
from Levenshtein import distance as lev

import tokenize_code_numbers

special_words = tokenize_code_numbers.code_numbers


def get_tokens(code):
    tokens = []
    cur_w = ''
    prev_w = ''
    counter = 0
    flag = False
    '''special = {'+', '-', '*', '/', ':', '=', '<', '>', '.', '(', ')', '[', ']',
               '{', '}', ':', ';', '\'', "\"", '$', '@', '#', '&', '^', '_', '~',
               '%', 'and', 'end', 'nil', 'set', 'array', 'file', 'not', 'then', 'begin', 'for',
               'of', 'to', 'case', 'function', 'or', 'type', 'const', 'goto', 'packed', 'until',
               'div', 'if', 'procedure', 'var', 'do', 'in', 'program', 'while',
               'downto', 'label', 'record', 'with', 'else', 'mod', 'repeat', 'writeln',
               'maxlongint', ';', 'maxint', 'read', 'integer', 'real', 'boolean', 'char', 'string',
               'Byte', 'ShortInt', 'Word', 'Integer', 'LongInt', 'Real', 'Single', 'Double', 'Extended',
               'Comp', 'Boolean', 'Char', 'Array', 'String', 'Record', 'Set', 'Text', 'File',
               '>=', '<=', 'or', 'not', 'xor', 'true', 'false', 'sin', 'cos', 'arctan', 'abs',
               'ln', 'exp', 'sqr', 'sqrt', 'pi', 'round', 'trunc', 'frac', 'random', 'odd', 'ord',
               'chr', 'pred', 'succ', 'readln', 'write', 'Assign', 'Reset', 'ReWrite', 'Append',
               'Close', 'Read', 'ReadLn', 'Write', 'WriteLn', ',', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}'''
    i = 0
    while i < len(code):
        if code[i] == '{':
            cur = '{'
            while i < len(code) and code[i] != '}':
                i += 1
                cur += code[i]
            i += 1
            print('comment', cur)
            tokens.append([tokenize_code_numbers.COMMENT_NUM, 1, cur])
        elif code[i] == "'":
            cur = "'"
            while i < len(code) and code[i] != "'":
                i += 1
                cur += code[i]
            i += 1
            print('string value', cur)
            tokens.append([tokenize_code_numbers.STRING_VALUE_NUM, 1, cur])
        elif cur_w == 'in' and i < len(code) - 1 and code[i] == 't':
            tokens.append([special_words['integer'], 1, 'integer'])
            i += 5
        elif cur_w == 'write' and i < len(code) - 1 and code[i] == 'l':
            tokens.append([special_words['writeln'], 1, 'writeln'])
            i += 2
        elif cur_w == 'Read' and i < len(code) - 1 and code[i] == 'L':
            tokens.append([special_words['ReadLn'], 1, 'ReadLn'])
            i += 2
        elif cur_w == 'Write' and i < len(code) - 1 and code[i] == 'L':
            tokens.append([special_words['WriteLn'], 1, 'WriteLn'])
            i += 2
        elif code[i] == ' ' or (code[i] in special_words.keys() and code[i] not in '0123456789'):
            elem = code[i]
            if cur_w != '':
                if cur_w in special_words.keys():
                    print('append', cur_w)
                    tokens.append([special_words[cur_w], 1, cur_w])
                else:
                    print('variable', cur_w)
                    tokens.append([tokenize_code_numbers.VARIABLE_NUM, 1, cur_w])
                cur_w = ''
            counter = 1
            while (i < len(code) - 1 and (
                    code[i + 1] == elem or (code[i + 1] in '0123456789' and elem in '0123456789'))):
                counter += 1
                i += 1
            if elem != ' ':
                tokens.append([special_words[elem], elem, counter])
            else:
                tokens.append([tokenize_code_numbers.SPACE_NUM, elem, counter])
            print('elem', elem, tokens[-1])
            cur_w = ''
        elif code[i] in special_words.keys() and code[i] in '0123456789':
            cur = code[i]
            i += 1
            while i < len(code) and code[i] in '0123456789':
                cur += code[i]
                i += 1
            tokens.append([tokenize_code_numbers.NUMBER_NUM, 1, cur])
            '''elif cur_w in special:
            while (i < len(code) and code[i] in '0123456789'):
                counter += 1
                i+=1
            tokens.append([cur_w, 1])
            cur_w = '''
        elif cur_w in special_words.keys():
            tokens.append([special_words[cur_w], 1, cur_w])
        else:
            cur_w += code[i]
        i += 1
    k = 1
    print(tokens)
    while k < len(tokens):
        if tokens[k][0] == tokens[k - 1][0]:
            print('remove', k, tokens[k])
            tokens.pop(k)
            k -= 1
            # print(tokens)
        elif tokens[k][0] == tokenize_code_numbers.NUMBER_NUM and tokens[k - 1][
                2] == tokenize_code_numbers.NUMBER_NUM:
            print('remove', k, tokens[k])
            tokens.pop(k)
            k -= 1
        elif tokens[k][2] == '=' and tokens[k - 1][2] == ':':
            tokens[k - 1] = [special_words[':=', 1, ':=']]
            print('remove', k, tokens[k])
            tokens.pop(k)
            k -= 1
        elif tokens[k][2] == '}':
            print('remove', k, tokens[k])
            tokens.pop(k)
            k -= 1
        k += 1
    return tokens


with open('test_code1.txt', 'r', encoding="utf-8") as file:
    code1 = file.read()
# code1 = format_code((code1))
with open('test_code3.txt', 'r', encoding="utf-8") as file:
    code2 = file.read()
# code2 = format_code(code2)
# print(code1)
t1 = get_tokens(code1)
t2 = get_tokens(code2)
print(t1)
print(t2)
i = 0
j = 0
flag = False
while i < len(t1) and j < len(t2):
    while i < len(t1) and t1[i][0] == tokenize_code_numbers.COMMENT_NUM or t1[i][
        0] == tokenize_code_numbers.SPACE_NUM or t1[i][
        0] == tokenize_code_numbers.STRING_VALUE_NUM:
        i += 1
    while j < len(t2) and t2[j][0] == tokenize_code_numbers.COMMENT_NUM or t2[j][
        0] == tokenize_code_numbers.SPACE_NUM or t2[j][
        0] == tokenize_code_numbers.STRING_VALUE_NUM:
        j += 1
    if t1[i][0] != t2[j][0]:
        print(i, j, t1[i][0], t2[j][0])
        flag = True
        break
    i += 1
    j += 1
if not flag:
    print('100 %')
'''if lev(code1, code2) == 0:
    print('100%')'''
