import re
from Levenshtein import distance as lev


def format_code(code):
    # code = code.replace('\n', '').replace('\r', '').replace('\t', '').replace(' ','')
    code = re.sub(r'\{[^\}]+\}', '', code)  # delete pascal comments
    # code = ' '.join(code.split())
    return code


def get_tokens(code):
    tokens = []
    cur_w = ''
    prev_w = ''
    counter = 0
    flag = False
    special = {'+', '-', '*', '/', ':', '=', '<', '>', '.', '(', ')', '[', ']',
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
               'Close', 'Read', 'ReadLn', 'Write', 'WriteLn', ',', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
    for i in range(len(code)):
        print(cur_w)
        if code[i] == ' ' or code[i] in special:
            elem = code[i]
            if cur_w != '':
                if cur_w in special:
                    print('append', cur_w)
                    tokens.append([cur_w, 1])
                else:
                    print('variable', cur_w)
                    tokens.append(['variable', 1])
                cur_w = ''
            counter = 0
            while (i < len(code) and (code[i] == elem or (code[i] in '0123456789' and elem in '0123456789'))):
                counter += 1
                i+=1
            tokens.append([elem, counter])
            cur_w = ''
        elif cur_w in special:
            while (i < len(code) and code[i] in '0123456789'):
                counter += 1
                i+=1
            tokens.append([cur_w, 1])
            cur_w = ''
        else:
            cur_w += code[i]
    i = 1
    while i < len(tokens):
        if tokens[i][0] == tokens[i - 1][0]:
            tokens.remove(tokens[i])
            i-=1
        i+=1
    return tokens


'''with open('test_code1.txt', 'r', encoding="utf-8") as file:
    code1 = file.read()'''
# code1 = format_code((code1))
with open('test_code2.txt', 'r', encoding="utf-8") as file:
    code2 = file.read()
code2 = format_code(code2)
# print(code1)
print(get_tokens(code2))
'''if lev(code1, code2) == 0:
    print('100%')'''
