# https://www.acmicpc.net/problem/12904
# 이름 : A와 B
# 번호 : 12904
# 난이도 : 골드 V
# 분류 : 구현, 문자열, 그리디 알고리즘

import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()
while len(S) < len(T):
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[:-1][::-1]
if S == T:
    print(1)
else:
    print(0)