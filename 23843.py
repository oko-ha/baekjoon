# https://www.acmicpc.net/problem/23843
# 이름 : 콘센트
# 번호 : 23843
# 난이도 : 골드 V
# 분류 : 자료 구조, 그리디 알고리즘, 정렬, 우선순위 큐

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, M = map(int, input().split())
device = sorted(list(map(int, input().split())))
outlet = [0] * M
while device:
    d = device.pop() + heappop(outlet)
    heappush(outlet, d)
print(max(outlet))