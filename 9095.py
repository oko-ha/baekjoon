# https://www.acmicpc.net/problem/9095
# 이름 : 1, 2, 3 더하기
# 번호 : 9095
# 난이도 : 실버 III
# 분류 : 다이나믹 프로그래밍

import sys
input = sys.stdin.readline
arr = [1, 2, 4]
t = 3
for _ in range(int(input())):
    n = int(input())
    if t < n:
        for i in range(t, n):
            arr.append(arr[i - 3] + arr[i - 2] + arr[i - 1])
        t = n
    print(arr[n - 1])