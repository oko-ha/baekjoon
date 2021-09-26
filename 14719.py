# https://www.acmicpc.net/problem/14719
# 이름 : 빗물
# 번호 : 14719
# 난이도 : 골드 V
# 분류 : 구현, 시뮬레이션

import sys
input = sys.stdin.readline
H, W = map(int, input().split())
arr = list(map(int, input().split()))
i = arr.index(max(arr))
def water(arr):
    t = m = 0
    for a in arr:
        if a > m:
            m = a
        t += m
    return t
print(water(arr[:i]) + water(arr[i:][::-1]) - sum(arr))