# https://www.acmicpc.net/problem/1927
# 이름 : 최소 힙
# 번호 : 1927
# 난이도 : 실버 I
# 분류 : 자료 구조, 우선순위 큐

import sys
import heapq
heap = []
for _ in range(int(sys.stdin.readline().rstrip())):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)