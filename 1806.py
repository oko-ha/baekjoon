# https://www.acmicpc.net/problem/1806
# 이름 : 부분합
# 번호 : 1806
# 난이도 : 골드 IV
# 분류 : 두 포인터

import sys
input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = float('inf')
temp = 0
i = -1
for j in range(N):
    temp += arr[j]
    if temp >= S:
        while i < j and temp >= S:
            i += 1
            temp -= arr[i]
        ans = min(ans, j - i + 1)
print(ans if ans < float('inf') else 0)