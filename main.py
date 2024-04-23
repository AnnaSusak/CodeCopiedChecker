import plagiate_checker
import os
import linter
from Levenshtein import distance as lev
from functools import cmp_to_key

RESULT_CODE_COPIED_FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + '/result_code_copied.txt'
RESULT_LINTER_FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + '/result_linter.txt'
SEPARATOR_LENGTH = 40
SEPARATOR = SEPARATOR_LENGTH * '-' + "\n"
directory = os.path.dirname(os.path.realpath(__file__))
files = []
res = ''
tokenized_files = []
linter_res = ''


def get_all_pascal_files_from_main_dir():
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f) and f.endswith('pas'):
            files.append(f)


def create_results_files_if_needed():
    pathes = [RESULT_CODE_COPIED_FILE_PATH, RESULT_CODE_COPIED_FILE_PATH]
    for path in pathes:
        if not os.path.exists(path):
            with open(path, 'w'): pass


def write_results_in_file(res_for_file, linter_res):
    with open(RESULT_CODE_COPIED_FILE_PATH, 'w', encoding="utf-8") as file:
        file.write(res_for_file)
    with open(RESULT_LINTER_FILE_PATH, 'w', encoding="utf-8") as file:
        file.write(linter_res)


def get_short_file_name(f1):
    return files[f1][files[f1].rfind('\\') + 1:]


def update_linter_res_for_file(linter_res):
    linter_res += SEPARATOR + get_short_file_name(f1) + '\n'
    errors = linter.get_error_lines(new_t)
    for i in errors:
        linter_res += str(i[0]) + ' ' + str(i[1]) + '\n'
    linter_res += SEPARATOR
    return linter_res


def tokens_to_str(t1):
    dist1 = ''
    for i in t1:
        dist1 += str(i[0]) + ' '
    return dist1


def get_plagiate_verdict_for_2_lsts_tokens(t1, t2):
    if plagiate_checker.check_2_codes(t1, t2) == 2:
        return '100 %'
    elif plagiate_checker.check_2_codes(t1, t2) == 1:
        return 'second level'
    else:
        dist1 = tokens_to_str(t1)
        dist2 = tokens_to_str(t2)
        return lev(dist1, dist2)


def get_plagiate_res_for_2_files(f1, f2):
    t1 = tokenized_files[f1]
    t2 = tokenized_files[f2]
    cur_res = [get_short_file_name(f1), get_short_file_name(f2)]
    cur_res.append(get_plagiate_verdict_for_2_lsts_tokens(t1, t2))
    return cur_res


def get_plagiate_result(tokenized_files):
    code_copied_res = []
    for f1 in range(0, len(tokenized_files) - 1):
        for f2 in range(f1 + 1, len(tokenized_files)):
            code_copied_res.append(get_plagiate_res_for_2_files(f1, f2))
    code_copied_res = sorted(code_copied_res, key=cmp_to_key(plagiate_checker.my_comp))
    return code_copied_res


def separate_different_plagiate_verdicts_if_needed(i):
    if i > 0 and code_copied_res[i - 1][2] != code_copied_res[i][2] and \
            code_copied_res[i - 1][2] in ['100 %', 'second level']:
        return SEPARATOR


def format_plagiate_check_results(code_copied_res):
    res_for_file = ''
    for i in range(len(code_copied_res)):
        res_for_file += separate_different_plagiate_verdicts_if_needed()
        res_for_file += str(code_copied_res[i][0]) + ' ' + str(code_copied_res[i][1]) + ' ' + str(code_copied_res[i][2]) \
                        + '\n'
    return res_for_file


get_all_pascal_files_from_main_dir()
create_results_files_if_needed()
for f1 in range(0, len(files)):
    with open(files[f1], 'r', encoding='utf-8-sig') as file:
        code1 = file.read()
        tokenized_files.append(plagiate_checker.get_tokens(code1))
        new_t = linter.get_tokens_for_linter(tokenized_files[-1])
        linter_res = update_linter_res_for_file(linter_res)
code_copied_res = get_plagiate_result(tokenized_files)
res_for_file = format_plagiate_check_results(code_copied_res)
write_results_in_file(res_for_file, linter_res)
