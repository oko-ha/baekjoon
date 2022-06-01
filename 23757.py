# https://www.acmicpc.net/problem/23757
# 이름 : 아이들과 선물 상자
# 번호 : 23737
# 난이도 : 실버 II
# 분류 : 자료 구조, 우선순위 큐

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, M = map(int, input().split())
gift = []
for n in map(int, input().split()):
    heappush(gift, -n)

def answer():
    for k in map(int, input().split()):
        n = -heappop(gift)
        if n - k < 0:
            return 0
        heappush(gift, -(n - k))
    return 1

print(answer())