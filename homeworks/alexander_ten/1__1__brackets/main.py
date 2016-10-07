import re
import sys


def brackets_check(s):
    meetings = 0
    br = ['[', ']', '(', ')', '{', '}']
    for c in s:
        if c == '(':
            meetings += 1
        elif c == ')':
            meetings -= 1
            if meetings < 0:
                return False

    return meetings == 0


str1 = "( cool qwerty 123 (ttt[ ) ] ( )rrr [qwerty {!!!@#$!@#$@! (*) &^%^&*!&%#} ] )) [][]  ([{ )"
pattern = re.findall(r'\[\d+\]', str1)
print(pattern)

pattern2 = re.sub(r'\([^)]*$', "", str1)
print(pattern2)

res = brackets_check(str1)
print(res)