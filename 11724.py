# https://www.acmicpc.net/problem/11724
# 이름 : 연결 요소의 개수
# 번호 : 11724
# 난이도 : 실버 II
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
visit = [0] * N
ans = 0
for i in range(N):
    if not visit[i]:
        ans += 1
        queue = deque([i])
        visit[i] = 1
        while queue:
            n = queue.popleft()
            for d in graph[n]:
                if not visit[d]:
                    visit[d] = 1
                    queue.append(d)
print(ans)