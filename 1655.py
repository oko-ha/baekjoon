# https://www.acmicpc.net/problem/1655
# 이름 : 가운데를 말해요
# 번호 : 1655
# 난이도 : 골드 II
# 분류 : 자료 구조, 우선순위 큐

import sys
import heapq
input = sys.stdin.readline
n = int(input())
leftHeap = [-int(input())]
rightHeap = []
print(-leftHeap[0])
for _ in range(n - 1):
    x = int(input())
    if x >= -leftHeap[0]:
        heapq.heappush(rightHeap, x)
    else:
        heapq.heappush(leftHeap, -x)
    if len(rightHeap) > len(leftHeap):
        heapq.heappush(leftHeap, -heapq.heappop(rightHeap))
    elif len(leftHeap) > len(rightHeap) + 1:
        heapq.heappush(rightHeap, -heapq.heappop(leftHeap))
    print(-leftHeap[0])