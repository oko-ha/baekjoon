# https://www.acmicpc.net/problem/11279
# 이름 : 최대 힙
# 번호 : 11279
# 난이도 : 실버 II
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
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-x, x))