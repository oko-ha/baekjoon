# https://www.acmicpc.net/problem/10844
# 이름 : 쉬운 계단 수
# 번호 : 10844
# 난이도 : 실버 I
# 분류 : 다이나믹 프로그래밍

import sys
n = int(sys.stdin.readline().rstrip())
number = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0] * 10]
for i in range(1, n):
    for j in range(10):
        if j == 0:
            number[i%2][j] = number[(i+1)%2][j + 1]
        elif j == 9:
            number[i%2][j] = number[(i+1)%2][j - 1]
        else:
            number[i%2][j] = number[(i+1)%2][j - 1] + number[(i+1)%2][j + 1]
print(sum(number[(n + 1)% 2]) % 1000000000)