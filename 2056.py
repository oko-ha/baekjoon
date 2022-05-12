# https://www.acmicpc.net/problem/2056
# 이름 : 작업
# 번호 : 2056
# 난이도 : 골드 IV
# 분류 : 다이나믹 프로그래밍, 그래프 이론, 위상 정렬

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
indegree = [0]
cost = [0]
for i in range(1, N + 1):
    arr = list(map(int, input().split()))
    cost.append(arr[0])
    indegree.append(arr[1])
    for j in range(arr[1]):
        graph[arr[2 + j]].append(i)
queue = deque()
ans = [0] * (N + 1)
for i in range(1, N + 1):
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
print(max(ans))