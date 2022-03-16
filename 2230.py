# https://www.acmicpc.net/problem/2230
# 이름 : 수 고르기
# 번호 : 2230
# 난이도 : 골드 V
# 분류 : 정렬, 두 포인터

import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
ans, j = INF, 0
for i in range(N):
    while j < N:
        if arr[j] - arr[i] >= M:
            ans = min(arr[j] - arr[i], ans)
            break
        j += 1
print(ans)