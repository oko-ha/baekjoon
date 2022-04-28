# https://www.acmicpc.net/problem/1374
# 이름 : 강의실
# 번호 : 1374
# 난이도 : 골드 V
# 분류 : 자료 구조, 그리디 알고리즘, 정렬, 우선순위 큐

import sys
from heapq import heappop, heappush, heappushpop
input = sys.stdin.readline

lecture = []
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    heappush(lecture, (b, c))
room = [0]
while lecture:
    start, end = heappop(lecture)
    if room[0] > start:
        heappush(room, end)
    else:
        heappushpop(room, end)
print(len(room))