# https://www.acmicpc.net/problem/19640
# 이름 : 화장실의 규칙
# 번호 : 19640
# 난이도 : 골드 V
# 분류 : 구현, 자료 구조, 시뮬레이션, 우선순위 큐

import sys
from heapq import heappop, heappush
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
head = []
line = [deque() for _ in range(M)]
for i in range(N):
    D, H = map(int, input().split())
    if i < M:
        heappush(head, (-D, -H, i, i))
    else:
        line[i % M].append((-D, -H, i % M, i))
ans = 0
while head[0][-1] != K:
    x, y, n, z = heappop(head)
    if line[n]:
        heappush(head, line[n].popleft())
    ans += 1
print(ans)