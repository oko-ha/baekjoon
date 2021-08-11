# https://www.acmicpc.net/problem/4097
# 이름 : 수익
# 번호 : 4097
# 난이도 : 실버 II
# 분류 : 다이나믹 프로그래밍

import sys
input = sys.stdin.readline
while True:
    n = int(input())
    if n == 0:
        break
    number = [int(input()) for _ in range(n)]
    ans = -float('inf')
    temp = 0
    maxVal = -float('inf')
    for num in number:
        temp += num
        if temp > maxVal:
            maxVal = temp
        if temp < 0:
            ans = max(ans, maxVal)
            temp = 0
            maxVal = -float('inf')
    print(max(ans, maxVal))