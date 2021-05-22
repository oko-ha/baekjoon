# https://www.acmicpc.net/problem/1182
# 이름 : 부분수열의 합
# 번호 : 1182
# 난이도 : 실버 II
# 분류 : 브루트포스 알고리즘, 백트래킹

import sys
from itertools import combinations
input = sys.stdin.readline
n, s = map(int, input().split())
num = list(map(int, input().split()))
ans = 0
for i in range(1, n + 1):
    for arr in list(combinations(num, i)):
        if sum(arr) == s:
            ans += 1
print(ans)