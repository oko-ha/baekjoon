# https://www.acmicpc.net/problem/1932
# 이름 : 정수 삼각형
# 번호 : 1932
# 난이도 : 실버 I
# 분류 : 다이나믹 프로그래밍

import sys
n = int(sys.stdin.readline().rstrip())
number = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(len(number)):
    if i > 0:
        for j in range(len(number[i])):
            if j == 0:
                number[i][0] += number[i - 1][0]
            elif j == len(number[i]) - 1:
                number[i][-1] += number[i - 1][-1]
            else:
                number[i][j] += max(number[i - 1][j - 1], number[i - 1][j])
print(max(number[-1]))