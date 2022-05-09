# https://www.acmicpc.net/problem/1516
# 이름 : 게임 개발
# 번호 : 1516
# 난이도 : 골드 III
# 분류 : 다이나믹 프로그래밍, 그래프 이론, 위상 정렬

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
cost = []
graph = [[] for _ in range(N)]
indegree = [0] * N
for i in range(N):
    arr = list(map(int, input().split()))
    cost.append(arr[0])
    for n in arr[1:-1]:
        graph[n-1].append(i)
        indegree[i] += 1
queue = deque()
ans = [0] * N
for i in range(N):
    if indegree[i] == 0:
        queue.append(i)
        ans[i] = cost[i]
while queue:
    nx = queue.popleft()
    for dx in graph[nx]:
        ans[dx] = max(ans[dx], ans[nx] + cost[dx])
        indegree[dx] -= 1
        if indegree[dx] == 0:
            queue.append(dx)
for a in ans:
    print(a)