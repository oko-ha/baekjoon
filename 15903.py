# https://www.acmicpc.net/problem/15903
# 이름 : 카드 합체 놀이
# 번호 : 15903
# 난이도 : 실버 II
# 분류 : 자료 구조, 그리디 알고리즘, 우선순위 큐

import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
heap = list(map(int, input().split()))
heapq.heapify(heap)
for _ in range(m):
    temp = heapq.heappop(heap) + heapq.heappop(heap)
    heapq.heappush(heap, temp)
    heapq.heappush(heap, temp)
print(sum(heap))