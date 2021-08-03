# https://www.acmicpc.net/problem/3986
# 이름 : 좋은 단어
# 번호 : 3986
# 난이도 : 실버 IV
# 분류 : 자료 구조, 문자열, 스택

import sys
input = sys.stdin.readline
ans = 0
for _ in range(int(input())):
    S = input().strip()
    stack = []
    for s in S:
        if not stack or stack[-1] != s:
            stack.append(s)
        else:
            stack.pop()
    if not stack:
        ans += 1
print(ans)