# https://www.acmicpc.net/problem/14241
# 이름 : 슬라임 합치기
# 번호 : 14241
# 난이도 : 실버 II
# 분류 : 수학, 자료 구조, 그리디 알고리즘, 우선순위 큐

import sys
import heapq
input = sys.stdin.readline
N = int(input())
heap = []
for a in list(map(int, input().split())):
    heapq.heappush(heap, -a)
ans = 0
while len(heap) > 1:
    x, y = heapq.heappop(heap), heapq.heappop(heap)
    ans += x * y
    heapq.heappush(heap, x + y)
print(ans)