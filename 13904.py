# https://www.acmicpc.net/problem/13904
# 이름 : 과제
# 번호 : 13904
# 난이도 : 골드 III
# 분류 : 자료 구조, 그리디 알고리즘, 우선순위 큐

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

arr = [0] * 1001
heap = []
for _ in range(int(input())):
    d, w = map(int, input().split())
    heappush(heap, (-w, d))
while heap:
    w, d = heappop(heap)
    for i in range(d, 0, -1):
        if arr[i] < -w:
            arr[i] = -w
            break
print(sum(arr))