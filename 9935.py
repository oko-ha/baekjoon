# https://www.acmicpc.net/problem/9935
# 이름 : 문자열 폭발
# 번호 : 9935
# 난이도 : 골드 IV
# 분류 : 자료 구조, 문자열, 스택

import sys
input = sys.stdin.readline
s = input().strip()
bomb = input().strip()
stack = []
temp = ''
i = cnt = 0
while i < len(s):
    if s[i] == bomb[0]:
        if len(temp) > 0:
            stack.append(temp)
            cnt += 1
        temp = s[i]
        if temp == bomb:
            temp = ''
    elif s[i] == bomb[len(temp)]:
        temp += s[i]
        if temp == bomb:
            if cnt > 0:
                temp = stack.pop()
                cnt -= 1
            else:
                temp = ''
    else:
        stack.append(temp)
        stack.append(s[i])
        temp = ''
    i += 1
stack.append(temp)
ans = ''.join(map(str, stack))
if ans == '':
    print('FRULA')
else:
    print(ans)