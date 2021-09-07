# https://www.acmicpc.net/problem/2470
# 이름 : 두 용액
# 번호 : 2470
# 난이도 : 골드 V
# 분류 : 이분 탐색, 두 포인터

import sys
input = sys.stdin.readline
N = int(input())
arr = sorted(list(map(int, input().split())))
m = float('inf')
i, j = 0, N - 1
while i < j:
    temp = arr[i] + arr[j]
    if abs(temp) < m:
        m = abs(temp)
        ans = [arr[i], arr[j]]
    if temp > 0:
        j -= 1
    elif temp < 0:
        i += 1
    else:
        break
print(*ans)