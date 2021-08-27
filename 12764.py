# https://www.acmicpc.net/problem/12764
# 이름 : 싸지방에 간 준하
# 번호 : 12764
# 난이도 : 골드 III
# 분류 : 구현, 자료 구조, 시뮬레이션, 우선순위 큐

import sys
import heapq
input = sys.stdin.readline
N = int(input())
people = []
for _ in range(N):
    P, Q = map(int, input().split())
    heapq.heappush(people, (P, Q))
a = 0
ans = [0 for _ in range(N)]
com = [0 for _ in range(N)]
while people:
    p, q = heapq.heappop(people)
    for i in range(len(com)):
        if p >= com[i]:
            if ans[i] == 0:
                a += 1
            ans[i] += 1
            com[i] = q
            break
print(a)
for an in ans:
    if an == 0:
        break
    print(an, end=' ')