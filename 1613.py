# https://www.acmicpc.net/problem/1613
# 이름 : 역사
# 번호 : 1613
# 난이도 : 골드 III
# 분류 : 그래프 이론, 플로이드-와샬

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0] * n for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    dp[a-1][b-1] = 1

def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] and dp[k][j]:
                    dp[i][j] = 1

floyd()
for _ in range(int(input())):
    a, b = map(int, input().split())
    if dp[a-1][b-1]:
        print(-1)
    elif dp[b-1][a-1]:
        print(1)
    else:
        print(0)