# https://www.acmicpc.net/problem/11060
# 이름 : 점프 점프
# 번호 : 11060
# 난이도 : 실버 II
# 분류 : 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
arr = list(map(int, input().split()))

def bfs():
    queue = deque([0])
    dp = [INF] * N
    dp[0] = 0
    while queue:
        nx = queue.popleft()
        if nx == N - 1:
            return dp[nx]
        for x in range(nx + 1, nx + 1 + arr[nx]):
            if x < N and dp[x] > dp[nx] + 1:
                dp[x] = dp[nx] + 1
                queue.append(x)
    return -1

print(bfs())