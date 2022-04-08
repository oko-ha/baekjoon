# https://www.acmicpc.net/problem/11000
# 이름 : 강의실 배정
# 번호 : 11000
# 난이도 : 골드 V
# 분류 : 자료 구조, 그리디 알고리즘, 정렬, 우선순위 큐

import sys
from heapq import heappush, heappushpop
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = sorted(arr, key = lambda x: x[0])
ans = [0]
for s, t in arr:
    if ans[0] > s:
        heappush(ans, t)
    else:
        heappushpop(ans, t)
print(len(ans))