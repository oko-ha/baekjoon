# https://www.acmicpc.net/problem/4949
# 이름 : 균형잡힌 세상
# 번호 : 4949
# 난이도 : 실버 IV
# 분류 : 자료 구조, 문자열, 스택

from sys import stdin
import re
from collections import Counter
while True:
    s = stdin.readline().rstrip()
    if s == '.':
        break
    s = re.findall('[\[\]\(\)]', s)
    c = Counter(s)
    if c['('] == c[')'] and c['['] == c[']']:
        if len(s) == 0:
            ans = 'yes'
        elif s[0] != ')' and s[0] != ']':
            ans = 'yes'
            stack = []
            for i in s:
                if i == ')':
                    if len(stack) == 0:
                        ans = 'no'
                        break
                    elif stack[-1] != '(':
                        ans = 'no'
                        break
                    else:
                        stack.pop(-1)
                elif i == ']':
                    if len(stack) == 0:
                        ans = 'no'
                        break
                    elif stack[-1] != '[':
                        ans = 'no'
                        break
                    else:
                        stack.pop(-1)
                else:
                    stack.append(i)
            if len(stack) != 0:
                ans = 'no'
        else:
            ans = 'no'
    else:
        ans = 'no'
    print(ans)