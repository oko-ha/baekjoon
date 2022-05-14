# https://www.acmicpc.net/problem/20119
# 이름 : 클레어와 물약
# 번호 : 20119
# 난이도 : 골드 I
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 위상 정렬

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [[] for _ in range(N + 1)]
for _ in range(M):
    arr = list(map(int, input().split()))
    for i in range(1, arr[0] + 1):
        graph[arr[i]].append((arr[-1], len(indegree[arr[-1]])))
    indegree[arr[-1]].append(arr[0])
L = int(input())
queue = deque(map(int, input().split()))
ans = set()
while queue:
    nx = queue.popleft()
    if nx in ans:
        continue
    ans.add(nx)
    for dx, i in graph[nx]:
        indegree[dx][i] -= 1
        if indegree[dx][i] == 0:
            queue.append(dx)
print(len(ans))
print(*sorted(ans))