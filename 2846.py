# https://www.acmicpc.net/problem/2846
# 이름 : 오르막길
# 번호 : 2846
# 난이도 : 브론즈 II
# 분류 : 구현

import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
ans = 0
first = last = 1000
for a in arr:
    if last < a:
        last = a
    else:
        ans = max(ans, last - first)
        first = a
        last = a
print(max(ans, last - first))