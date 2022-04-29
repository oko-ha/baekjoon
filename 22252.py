# https://www.acmicpc.net/problem/22252
# 이름 : 정보 상인 호석
# 번호 : 22252
# 난이도 : 골드 V
# 분류 : 자료 구조, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵, 우선순위 큐

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

trader = dict()
ans = 0
for _ in range(int(input())):
    q = list(input().split())
    if q[0] == '1':
        if q[1] not in trader:
            trader[q[1]] = []
        for C in list(map(int, q[3:])):
            heappush(trader[q[1]], -C)
    elif q[0] == '2':
        if q[1] in trader:
            for _ in range(int(q[2])):
                if trader[q[1]]:
                    ans -= heappop(trader[q[1]])
                else:
                    break
print(ans)