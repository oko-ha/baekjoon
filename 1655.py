# https://www.acmicpc.net/problem/1655
# 이름 : 가운데를 말해요
# 번호 : 1655
# 난이도 : 골드 II
# 분류 : 

import sys
import heapq
heap = []
for _ in range(int(sys.stdin.readline().rstrip())):
    x = int(sys.stdin.readline().rstrip())
    heapq.heappush(heap, (x, x))