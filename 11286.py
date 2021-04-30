# https://www.acmicpc.net/problem/11286
# 이름 : 절댓값 힙
# 번호 : 11286
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
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(x), x))