# https://www.acmicpc.net/problem/2252
# 이름 : 줄 세우기
# 번호 : 2252
# 난이도 : 골드 III
# 분류 : 그래프 이론, 위상 정렬

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1
queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
ans = []
while queue:
    nx = queue.popleft()
    ans.append(nx)
    for dx in graph[nx]:
        indegree[dx] -= 1
        if indegree[dx] == 0:
            queue.append(dx)
print(*ans)