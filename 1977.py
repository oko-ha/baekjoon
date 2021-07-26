# https://www.acmicpc.net/problem/1977
# 이름 : 완전제곱수
# 번호 : 1977
# 난이도 : 브론즈 I
# 분류 : 수학, 구현

import sys
from math import ceil
input = sys.stdin.readline
M = int(input())
N = int(input())
arr = [i ** 2 for i in range(ceil(M ** 0.5), int(N ** 0.5) + 1)]
if len(arr) > 0:
    print(sum(arr))
    print(arr[0])
else:
    print(-1)