# https://www.acmicpc.net/problem/1504
# 이름 : 특정한 최단 경로
# 번호 : 1504
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 다익스트라

import sys
import heapq
input = sys.stdin.readline
N, E = map(int, input().split())
graph = {i + 1 : {} for i in range(N)}
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
v1, v2 = map(int, input().split())
def dijkstra(start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    while queue:
        current_distance, current_destination = heapq.heappop(queue)
        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
    return distances
first = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)
ans = min(first[v1] + v1_[v2] + v2_[N], first[v2] + v2_[v1] + v1_[N])
print(ans if ans < float('inf') else -1)