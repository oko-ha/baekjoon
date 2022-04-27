# https://www.acmicpc.net/problem/21939
# 이름 : 문제 추천 시스템 Version 1
# 번호 : 21939
# 난이도 : 골드 IV
# 분류 : 자료 구조, 트리를 사용한 집합과 맵, 우선순위 큐

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

minHeap = []
maxHeap = []
key = dict()
for _ in range(int(input())):
    P, L = map(int, input().split())
    heappush(minHeap, (L, P))
    heappush(maxHeap, (-L, -P))
    key[P] = False
for _ in range(int(input())):
    order = list(input().split())
    if order[0] == 'recommend':
        if order[1] == '1':
            print(-maxHeap[0][1])
        elif order[1] == '-1':
            print(minHeap[0][1])
    elif order[0] == 'add':
        heappush(minHeap, (int(order[2]), int(order[1])))
        heappush(maxHeap, (-int(order[2]), -int(order[1])))
        key[int(order[1])] = False
    elif order[0] == 'solved':
        key[int(order[1])] = True
        while key[-maxHeap[0][1]]:
            heappop(maxHeap)
        while key[minHeap[0][1]]:
            heappop(minHeap)