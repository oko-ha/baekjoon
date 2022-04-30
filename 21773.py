# https://www.acmicpc.net/problem/21773
# 이름 : 가희와 프로세스 1
# 번호 : 21773
# 난이도 : 골드 V
# 분류 : 자료 구조, 우선순위 큐

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

T, n = map(int, input().split())
proc = []
for _ in range(n):
    A, B, C = map(int, input().split())
    heappush(proc, (-C, A, B))
for _ in range(T):
    C, A, B = heappop(proc)
    print(A)

    if B - 1 > 0:
        heappush(proc, (C + 1, A, B - 1))