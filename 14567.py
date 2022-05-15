# https://www.acmicpc.net/problem/14567
# 이름 : 선수과목 (Prerequisite)
# 번호 : 14567
# 난이도 : 골드 V
# 분류 : 다이나믹 프로그래밍, 그래프 이론, 위상 정렬

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
indegree = [0] * N
for _ in range(M):
    A, B = map(int, input().split())
    graph[A-1].append(B-1)
    indegree[B-1] += 1
queue = deque()
for i in range(N):
    if indegree[i] == 0:
        queue.append((i, 1))
ans = [0] * N
while queue:
    nx, term = queue.popleft()
    ans[nx] = term
    for dx in graph[nx]:
        indegree[dx] -= 1
        if indegree[dx] == 0:
            queue.append((dx, term + 1))
print(*ans)