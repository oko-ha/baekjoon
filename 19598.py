# https://www.acmicpc.net/problem/19598
# 이름 : 최소 회의실 개수
# 번호 : 19598
# 난이도 : 골드 V
# 분류 : 자료 구조, 그리디 알고리즘, 정렬, 스위핑, 우선순위 큐

import sys
from heapq import *
input = sys.stdin.readline

conf = []
for _ in range(int(input())):
    start, end = map(int, input().split())
    heappush(conf, (start, end))
room = [0]
while conf:
    start, end = heappop(conf)
    if room[0] > start:
        heappush(room, end)
    else:
        heappushpop(room, end)
print(len(room))