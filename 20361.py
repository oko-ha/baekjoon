# https://www.acmicpc.net/problem/20361
# 이름 : 일우는 야바위꾼
# 번호 : 20361
# 난이도 : 브론즈 III
# 분류 : 구현, 시뮬레이션

import sys
input = sys.stdin.readline
N, X, K = map(int, input().split())
ball = X
for _ in range(K):
    a, b = map(int , input().split())
    if ball == a:
        ball = b
    elif ball == b:
        ball = a
print(ball)