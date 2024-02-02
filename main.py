import re
from Levenshtein import distance as lev





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
    i = 0
    while i < len(code):
        #print(cur_w)
        if code[i] == '{':
            cur = '{'
            while i < len(code) and code[i] != '}':
                i+=1
                cur += code[i]
            i+=1
            print ('comment', cur)
            tokens.append(['comment', 1])
        elif code[i] == "'":
            cur = "'"
            while i < len(code) and code[i] != "'":
                i+=1
                cur += code[i]
            i+=1
            print ('string value', cur)
            tokens.append(['string value', 1])
        elif cur_w == 'in' and i < len(code) - 1 and code[i] =='t':
            tokens.append(['integer', 1])
            i += 5
        elif cur_w == 'write' and i < len(code) - 1 and code[i] == 'l':
            tokens.append(['writeln', 1])
            i+=2
        elif code[i] == ' ' or (code[i] in special and code[i] not in '0123456789'):
            elem = code[i]
            if cur_w != '':
                if cur_w in special:
                    print('append', cur_w)
                    tokens.append([cur_w, 1])
                else:
                    print('variable', cur_w)
                    tokens.append(['variable', 1])
                cur_w = ''
            counter = 1
            while (i < len(code) - 1 and (code[i + 1] == elem or (code[i + 1] in '0123456789' and elem in '0123456789'))):
                counter += 1
                i+=1
            tokens.append([elem, counter])
            print('elem', elem, tokens[-1])
            cur_w = ''
        elif code[i] in special and code[i] in '0123456789':
            cur = code[i]
            i +=1
            while i < len(code) and code[i] in '0123456789':
                cur += code[i]
                i+=1
            tokens.append([cur, 1])
            '''elif cur_w in special:
            while (i < len(code) and code[i] in '0123456789'):
                counter += 1
                i+=1
            tokens.append([cur_w, 1])
            cur_w = '''
        elif cur_w in special:
            tokens.append([cur_w, 1])
        else:
            cur_w += code[i]
        i+=1
    k = 1
    print(tokens)
    while k < len(tokens):
        if tokens[k][0] == tokens[k - 1][0]:
            print('remove', k, tokens[k])
            tokens.pop(k)
            k-=1
           # print(tokens)
        elif tokens[k][0][0] in '0123456789' and tokens[k- 1][0][0] in '0123456789':
            print('remove', k, tokens[k])
            tokens.pop(k)
            k -= 1
        elif tokens[k][0] == '=' and tokens[k-1][0] ==':':
            tokens[k - 1][0] = ':='
            print('remove', k, tokens[k])
            tokens.pop(k)
            k -= 1
        elif tokens[k][0] == '}':
            print('remove', k, tokens[k])
            tokens.pop(k)
            k-=1
        k+=1
    return tokens


with open('test_code1.txt', 'r', encoding="utf-8") as file:
    code1 = file.read()
# code1 = format_code((code1))
with open('test_code3.txt', 'r', encoding="utf-8") as file:
    code2 = file.read()
#code2 = format_code(code2)
# print(code1)
t1=get_tokens(code1)
t2=get_tokens(code2)
print(t1)
print(t2)
i = 0
j = 0
flag = False
while i < len(t1) and j < len(t2):
    while i < len(t1) and t1[i][0] == 'comment' or t1[i][0] == ' ' or t1[i][0] == 'string value':
        i+=1
    while j < len(t2) and t2[j][0] == 'comment' or t2[j][0] == ' ' or t2[i][0] == 'string value':
        j+=1
    if t1[i][0] != t2[j][0]:
        print(i, j, t1[i][0], t2[j][0])
        flag = True
        break
    i+=1
    j+=1
if not flag:
    print('100 %')
'''if lev(code1, code2) == 0:
    print('100%')'''
