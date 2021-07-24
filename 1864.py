# https://www.acmicpc.net/problem/1864
# 이름 : 문어 숫자
# 번호 : 1864
# 난이도 : 브론즈 III
# 분류 : 수학, 구현, 사칙연산

import sys
dic = {'-':0, '\\':1, '(':2, '@':3, '?':4, '>':5, '&':6, '%':7, '/':-1}
while True:
    S = sys.stdin.readline().strip()
    if S == '#':
        break
    ans = 0
    for i in range(len(S)):
        ans += (8 ** (len(S) - 1 - i)) * dic[S[i]]
    print(ans)