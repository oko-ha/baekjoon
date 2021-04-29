# https://www.acmicpc.net/problem/11054
# 이름 : 가장 긴 바이토닉 부분 수열
# 번호 : 11054
# 난이도 : 골드 III
# 분류 : 다이나믹 프로그래밍

import sys
n = int(sys.stdin.readline().rstrip())
number = list(map(int, sys.stdin.readline().split()))
toRight = [1 for _ in range(n)]
toLeft = [1 for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        if number[i] < number[j]:
            if toRight[i] + 1 > toRight[j]:
                toRight[j] = toRight[i] + 1
for i in range(n - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        if number[i] < number[j]:
            if toLeft[i] + 1 > toLeft[j]:
                toLeft[j] = toLeft[i] + 1
ans = []
for i in range(n):
    ans.append(toRight[i] + toLeft[i])
print(max(ans)-1)