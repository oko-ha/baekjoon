# https://www.acmicpc.net/problem/1766
# 이름 : 문제집
# 번호 : 1766
# 난이도 : 골드 II
# 분류 : 그래프 이론, 자료 구조, 우선순위 큐, 위상 정렬

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1
heap = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        heappush(heap, i)
answer = []
while heap:
    current = heappop(heap)
    answer.append(current)
    for i in graph[current]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heappush(heap, i)
print(*answer)