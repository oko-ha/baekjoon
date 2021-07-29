# https://www.acmicpc.net/problem/1202
# 이름 : 보석 도둑
# 번호 : 1202
# 난이도 : 골드 II
# 분류 : 자료 구조, 그리디 알고리즘, 정렬, 우선순위 큐

import sys
import heapq
input = sys.stdin.readline
N, K = map(int, input().split())
jewel = []
for _ in range(N):
    M, V = map(int, input().split())
    heapq.heappush(jewel, (M, V))
pack = []
for _ in range(K):
    heapq.heappush(pack, int(input()))
ans = 0
temp = []
while pack and (jewel or temp):
    p = heapq.heappop(pack)
    while jewel and p >= jewel[0][0]:
        m, v = heapq.heappop(jewel)
        heapq.heappush(temp, -v)
    if temp:
        ans -= heapq.heappop(temp)
print(ans)