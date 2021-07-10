# https://www.acmicpc.net/problem/12738
# 이름 : 가장 긴 증가하는 부분 수열 3
# 번호 : 12739
# 난이도 : 골드 II
# 분류 : 이분 탐색, 가장 긴 증가하는 부분 수열: o(n log n)

import sys
from bisect import bisect_left
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
lis = [arr[0]]
for i in range(1, n):
    if lis[-1] < arr[i]:
        lis.append(arr[i])
    else:
        lis[bisect_left(lis, arr[i])] = arr[i]
print(len(lis))