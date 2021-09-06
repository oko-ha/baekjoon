# https://www.acmicpc.net/problem/3273
# 이름 : 두 수의 합
# 번호 : 3273
# 난이도 : 실버 III
# 분류 : 정렬, 두 포인터

import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())
ans = 0
i, j = 0, n - 1
while i < j:
    s = arr[i] + arr[j]
    if s == x:
        ans += 1
    if s > x:
        j -= 1
    else:
        i += 1
print(ans)