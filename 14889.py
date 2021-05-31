# https://www.acmicpc.net/problem/14889
# 이름 : 스타트와 링크
# 번호 : 14889
# 난이도 : 실버 III
# 분류 : 브루트포스 알고리즘, 백트래킹

import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
d = deque(combinations([i for i in range(n)], n // 2))
ans = []
for _ in range(len(d) // 2):
    a = 0
    for x, y in combinations(d.popleft(), 2):
        a += arr[x][y] + arr[y][x]
    b = 0
    for x, y in combinations(d.pop(), 2):
        b += arr[x][y] + arr[y][x]
    ans.append(abs(a - b))
print(min(ans))