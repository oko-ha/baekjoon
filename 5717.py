# https://www.acmicpc.net/problem/5717
# 이름 : 상근이의 친구들
# 번호 : 5717
# 난이도 : 브론즈 III
# 분류 : 수학, 사칙연산

import sys
while True:
    M, F = map(int, sys.stdin.readline().split())
    if M == F == 0:
        break
    print(M + F)