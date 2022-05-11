# https://www.acmicpc.net/problem/2623
# 이름 : 음악프로그램
# 번호 : 2623
# 난이도 : 골드 II
# 분류 : 그래프 이론, 위상 정렬

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(M):
    arr = list(map(int, input().split()))
    for i in range(1, arr[0]):
        graph[arr[i]].append(arr[i + 1])
        indegree[arr[i + 1]] += 1
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
if len(ans) == N:
    for a in ans:
        print(a)
else:
    print(0)