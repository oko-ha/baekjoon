# https://www.acmicpc.net/problem/2512
# 이름 : 예산
# 번호 : 2512
# 난이도 : 실버 III
# 분류 : 이분 탐색

import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
left, right = 0, max(arr)
while left <= right:
    mid = (left + right) // 2
    temp = 0
    for a in arr:
        if a < mid:
            temp += a
        else:
            temp += mid
    if temp > M:
        right = mid - 1
    else:
        left = mid + 1
print(right)