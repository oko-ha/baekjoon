# https://www.acmicpc.net/problem/7662
# 이름 : 이중 우선순위 큐
# 번호 : 7662
# 난이도 : 골드 V
# 분류 : 자료 구조, 트리를 사용한 집합과 맵, 우선순위 큐

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

for _ in range(int(input())):
    max_heap, min_heap, check, index = [], [], [], 0
    for _ in range(int(input())):
        cmd, n = input().split()
        n = int(n)
        if cmd == 'I':
            heappush(max_heap, (-n, index))
            heappush(min_heap, (n, index))
            check.append(False)
            index += 1
        elif cmd == 'D':
            if n == 1:
                while max_heap and check[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    check[max_heap[0][1]] = True
                    heappop(max_heap)
            elif n == -1:
                while min_heap and check[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    check[min_heap[0][1]] = True
                    heappop(min_heap)
    while max_heap and check[max_heap[0][1]]:
        heappop(max_heap)
    while min_heap and check[min_heap[0][1]]:
        heappop(min_heap)
    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')