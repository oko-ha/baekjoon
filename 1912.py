# https://www.acmicpc.net/problem/1912
# 이름 : 연속합
# 번호 : 1912
# 난이도 : 실버 II
# 분류 : 다이나믹 프로그래밍

import sys
n = int(sys.stdin.readline().rstrip())
number = list(map(int, sys.stdin.readline().split()))
m = []
i = 0
temp = 0
maxVal = -1000
for i in range(n):
    temp += number[i]
    if temp > maxVal:
        maxVal = temp
    if temp < 0:
        m.append(maxVal)
        temp = 0
        maxVal = -1000
m.append(maxVal)
print(max(m))