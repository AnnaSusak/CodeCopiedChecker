import re


def format_code(code):
    code = code.replace('\n', '').replace('\r', '').replace('\t', '')
    re.sub(r'\{[^\}]+\}', '', code)  # delete pascal comments
    code = ' '.join(code.split())
    return code


with open('test_code1.txt', 'r', encoding="utf-8") as file:
    code1 = file.read()
code1 = format_code((code1))
print(code1)
