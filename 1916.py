# https://www.acmicpc.net/problem/1916
# 이름 : 최소비용 구하기
# 번호 : 1916
# 난이도 : 골드 V
# 분류 : 그래프 이론, 다익스트라

import sys
import heapq
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = {i + 1 : {} for i in range(N)}
for _ in range(M):
    a, b, c = map(int, input().split())
    if b in graph[a]:
        graph[a][b] = min(c, graph[a][b])
    else:
        graph[a][b] = c
start, end = map(int, input().split())
def dijkstra(graph, start):
    dists = {node : float('inf') for node in graph}
    dists[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        cur_dist, cur_dest = heapq.heappop(queue)
        if dists[cur_dest] < cur_dist:
            continue
        for new_dest, new_dist in graph[cur_dest].items():
            dist = cur_dist + new_dist
            if dist < dists[new_dest]:
                dists[new_dest] = dist
                heapq.heappush(queue, (dist, new_dest))
    return dists
print(dijkstra(graph, start)[end])
