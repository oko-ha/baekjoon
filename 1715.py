# https://www.acmicpc.net/problem/1715
# 이름 : 카드 정렬하기
# 번호 : 1715
# 난이도 : 골드 IV
# 분류 : 자료 구조, 그리디 알고리즘, 우선순위 큐

import sys
import heapq
input = sys.stdin.readline
heap = []
for _ in range(int(input())):
    heapq.heappush(heap, int(input()))
ans = 0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    ans += a + b
    heapq.heappush(heap, a + b)
print(ans)
