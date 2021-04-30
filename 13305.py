# https://www.acmicpc.net/problem/13305
# 이름 : 주유소
# 번호 : 13305
# 난이도 : 실버 IV
# 분류 : 그리디 알고리즘

import sys
n = int(sys.stdin.readline().rstrip())
road = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))
ans = 0
p = price[0]
r = 0
for i in range(n - 1):
    r += road[i]
    if p > price[i + 1]: # 다음 주유소가 더 싸면
        ans += p * r
        p = price[i + 1]
        r = 0
print(ans + p * r)