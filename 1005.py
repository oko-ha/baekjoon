# https://www.acmicpc.net/problem/1005
# 이름 : 골드 III
# 번호 : 1005
# 난이도 : 골드 III
# 분류 : 다이나믹 프로그래밍, 그래프 이론, 위상 정렬

import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    graph = [[] for _ in range(N)]
    indegree = [0] * N
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X - 1].append(Y - 1)
        indegree[Y - 1] += 1
    W = int(input()) - 1
    queue = deque()
    ans = [0] * N
    for i in range(N):
        if indegree[i] == 0:
            queue.append(i)
            ans[i] = D[i]
    while queue:
        nx = queue.popleft()
        if nx == W:
            break
        for dx in graph[nx]:
            indegree[dx] -= 1
            ans[dx] = max(ans[dx], ans[nx] + D[dx])
            if indegree[dx] == 0:
                queue.append(dx)
    print(ans[W])