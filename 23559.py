# https://www.acmicpc.net/problem/23559
# 이름 : 밥
# 번호 : 23559
# 난이도 : 골드 V
# 분류 : 자료 구조, 그리디 알고리즘, 정렬, 우선순위 큐

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, X = map(int, input().split())
ans = 0
heap = []
for _ in range(N):
    A, B = map(int, input().split())
    if A > B:
        heappush(heap, (B - A, A, B))
    else:
        ans += B
        N -= 1
        X -= 1000
while heap and X - (len(heap) - 1) * 1000 >= 5000:
    t, a, b = heappop(heap)
    ans += a
    X -= 5000
for t, a, b in heap:
    ans += b
print(ans)