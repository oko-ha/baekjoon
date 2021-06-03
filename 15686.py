# https://www.acmicpc.net/problem/15686
# 이름 : 치킨 배달
# 번호 : 15686
# 난이도 : 골드 V
# 분류 : 구현, 브루트포스 알고리즘

import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
chicken = []
house = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i, j))
        if city[i][j] == 1:
            house.append((i, j))
ans = []
for selection in list(combinations(chicken, m)):
    temp = 0
    for h in house:
        temp += min([abs(h[0]-s[0]) + abs(h[1]-s[1]) for s in selection])
    ans.append(temp)
print(min(ans))