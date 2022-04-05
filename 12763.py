# https://www.acmicpc.net/problem/12763
# 이름 : 지각하면 안 돼
# 번호 : 12763
# 난이도 : 골드 II
# 분류 : 그래프 이론, 그래프 탐색, 깊이 우선 탐색, 다익스트라

import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
T, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    graph[a-1].append((d, c, b-1))
    graph[b-1].append((d, c, a-1))
ans = INF
def dfs(nx, n_money, n_time):
    global ans
    if nx == N - 1:
        ans = min(ans, n_money)
        return
    for d_money, d_time, dx in graph[nx]:
        money, time = n_money + d_money, n_time + d_time
        if money <= M and time <= T:
            dfs(dx, money, time)
dfs(0, 0, 0)
if ans < INF:
    print(ans)
else:
    print(-1)