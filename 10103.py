# https://www.acmicpc.net/problem/10103
# 이름 : 주사위 게임
# 번호 : 10103
# 난이도 : 브론즈 III
# 분류 : 수학, 구현, 사칙연산

import sys
input = sys.stdin.readline
a = b = 100
for _ in range(int(input())):
    c, d = map(int, input().split())
    if c > d:
        b -= c
    elif c < d:
        a -= d
print('{}\n{}'.format(a, b))