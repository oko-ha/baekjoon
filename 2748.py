# https://www.acmicpc.net/problem/2748
# 이름 : 피보나치 수 2
# 번호 : 2748
# 난이도 : 브론즈 I
# 분류 : 수학, 다이나믹 프로그래밍

import sys
n = int(sys.stdin.readline())
x, y = 0, 1
for _ in range(n):
    x, y = y, x + y
print(x)