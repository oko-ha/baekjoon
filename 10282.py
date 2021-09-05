# https://www.acmicpc.net/problem/10282
# 이름 : 해킹
# 번호 : 10282
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 다익스트라

import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = sys.maxsize
for _ in range(int(input())):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b-1].append((s, a-1))
    dp = [INF] * n
    dp[c-1] = 0
    heap = []
    heappush(heap, (0, c-1))
    while heap:
        ns, nx = heappop(heap)
        for ds, dx in graph[nx]:
            time = ns + ds
            if dp[dx] > time:
                dp[dx] = time
                heappush(heap, (time, dx))
    ans = [0, 0]
    for d in dp:
        if d < INF:
            ans[0] += 1
            ans[1] = max(ans[1], d)
    print(*ans)