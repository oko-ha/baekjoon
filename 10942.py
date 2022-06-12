# https://www.acmicpc.net/problem/10942
# 이름 : 팰린드롬?
# 번호 : 10942
# 난이도 : 골드 IV
# 분류 : 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))
dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N):
    for s in range(1, N + 1 - i):
        e = s + i
        if s == e:
            dp[s][e] = 1
        elif arr[s] == arr[e]:
            if s + 1 == e:
                dp[s][e] = 1
            elif dp[s + 1][e - 1]:
                dp[s][e] = 1
for _ in range(int(input())):
    s, e = map(int, input().split())
    print(dp[s][e])