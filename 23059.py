# https://www.acmicpc.net/problem/23059
# 이름 : 리그 오브 레게노
# 번호 : 23059
# 난이도 : 골드 II
# 분류 : 그래프 이론, 자료 구조, 해시를 사용한 집합과 맵, 위상 정렬

import sys
from collections import defaultdict
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
graph = defaultdict(list)
indegree = dict()
for _ in range(N):
    A, B = input().split()
    graph[A].append(B)
    if A not in indegree:
        indegree[A] = 0
    if B not in indegree:
        indegree[B] = 1
    else:
        indegree[B] += 1
heap, temp = [], []
ans = []
for key, value in indegree.items():
    if value == 0:
        heappush(temp, key)
while temp:
    heap += temp
    temp = []
    while heap:
        nx = heappop(heap)
        ans.append(nx)
        for dx in graph[nx]:
            indegree[dx] -= 1
            if indegree[dx] == 0:
                heappush(temp, dx)
if len(ans) == len(indegree):
    for a in ans:
        print(a)
else:
    print(-1)