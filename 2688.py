# https://www.acmicpc.net/problem/2688
# 이름 : 줄어들지 않아
# 번호 : 2688
# 난이도 : 골드 V
# 분류 : 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

arr = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
for _ in range(int(input())):
    n = int(input())
    while len(arr) < n:
        arr.append([sum(arr[-1])])
        for i in range(9):
            arr[-1].append(arr[-1][-1] - arr[-2][i])
    print(sum(arr[n-1]))