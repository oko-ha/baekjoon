# https://www.acmicpc.net/problem/1826
# 이름 : 연료 채우기
# 번호 : 1826
# 난이도 : 골드 III
# 분류 : 자료 구조, 그리디 알고리즘, 정렬, 우선순위 큐

import sys
import heapq
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))
arr.sort()
L, P = map(int, input().split())
def fill(L, P, arr):
    heap = []
    cnt = 0
    for a, b in arr:
        if P >= L:
            break
        while a > P:
            if len(heap) == 0:
                return -1
            P += heapq.heappop(heap)[1]
            cnt += 1
        heapq.heappush(heap, (-b, b))
    while P < L:
        if len(heap) == 0:
            return - 1
        P += heapq.heappop(heap)[1]
        cnt += 1
    return cnt
print(fill(L, P, arr))