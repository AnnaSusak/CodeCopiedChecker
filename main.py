import plagiate_checker
import os
import linter
from Levenshtein import distance as lev
from functools import cmp_to_key

RESULT_CODE_COPIED_FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + '/result_code_copied.txt'
RESULT_LINTER_FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + '/result_linter.txt'

directory = os.path.dirname(os.path.realpath(__file__))
files = []
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and f.endswith('pas'):
        files.append(f)
if not os.path.exists(RESULT_CODE_COPIED_FILE_PATH):
    with open(RESULT_CODE_COPIED_FILE_PATH, 'w'): pass
res = ''
code_copied_res = []
tokenized_files = []
linter_res = ''
for f1 in range(0, len(files)):
    with open(files[f1], 'r', encoding='utf-8-sig') as file:
        code1 = file.read()
        tokenized_files.append(plagiate_checker.get_tokens(code1))
        new_t = linter.get_tokens_for_linter(tokenized_files[-1])
        linter_res += "-" * 40 + "\n" + files[f1][files[f1].rfind('\\') + 1:] + '\n'
        errors = linter.get_error_lines(new_t)
        for i in errors:
            linter_res += str(i[0]) + ' ' +str(i[1]) + '\n'
        linter_res += "-" * 40
for f1 in range(0, len(tokenized_files) - 1):
    for f2 in range(f1 + 1, len(tokenized_files)):
        t1 = tokenized_files[f1]
        t2 = tokenized_files[f2]
        cur_res = [files[f1][files[f1].rfind('\\') + 1:], files[f2][files[f2].rfind('\\') + 1:]]
        if plagiate_checker.check_2_codes(t1, t2) == 2:
            cur_res.append('100 %')
        elif plagiate_checker.check_2_codes(t1, t2) == 1:
            cur_res.append('second level')
        else:
            dist1 = ''
            dist2 = ''
            for i in t1:
                dist1 += str(i[0]) + ' '
            for j in t2:
                dist2 += str(j[0]) + ' '
            cur_res.append(lev(dist1, dist2))
        code_copied_res.append(cur_res)
code_copied_res=sorted(code_copied_res, key=cmp_to_key(plagiate_checker.my_comp))
res_for_file = ''
for i in range(len(code_copied_res)):
    if i > 0 and code_copied_res[i - 1][2] != code_copied_res[i][2] and \
         code_copied_res[i - 1][2] in ['100 %', 'second level']:
        res_for_file += '-' * 40 + '\n'
    res_for_file += str(code_copied_res[i][0]) + ' ' + str(code_copied_res[i][1]) + ' ' + str(code_copied_res[i][2])\
                    + '\n'
with open(RESULT_CODE_COPIED_FILE_PATH, 'w', encoding="utf-8") as file:
    file.write(res_for_file)
with open(RESULT_LINTER_FILE_PATH, 'w', encoding="utf-8") as file:
    file.write(linter_res)
