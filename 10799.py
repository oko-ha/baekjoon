# https://www.acmicpc.net/problem/10799
# 이름 : 쇠막대기
# 번호 : 10799
# 난이도 : 실버 III
# 분류 : 자료 구조, 스택

import sys
s = sys.stdin.readline().strip()
stack = []
ans = 0
i = 0
while i < len(s) - 1:
    if s[i] == '(':
        if s[i + 1] == ')':
            ans += len(stack)
            i += 1
        else:
            stack.append('(')
    else:
        stack.pop()
        ans += 1
    i += 1
print(ans + 1)