# https://www.acmicpc.net/problem/2637
# 이름 : 장난감 조립
# 번호 : 2637
# 난이도 : 골드 II
# 분류 : 다이나믹 프로그래밍, 그래프 이론, 위상 정렬

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(int(input())):
    X, Y, K = map(int, input().split())
    graph[X].append((Y, K))
    indegree[Y] += 1
queue = deque()
ans = [0] * (N + 1)
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
        ans[i] = 1
while queue:
    nx = queue.popleft()
    for dx, cost in graph[nx]:
        indegree[dx] -= 1
        ans[dx] += ans[nx] * cost
        if indegree[dx] == 0:
            queue.append(dx)
for i in range(1, N + 1):
    if not graph[i]:
        print(i, ans[i])