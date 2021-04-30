# https://www.acmicpc.net/problem/11047
# 이름 : 동전 0
# 번호 : 11047
# 난이도 : 실버 II
# 분류 : 그리디 알고리즘

import sys
n, k = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
cnt = 0
for i in range(n - 1, -1, -1):
    if k >= coin[i]:
        cnt += k // coin[i]
        k %= coin[i]
    if k == 0:
        break
print(cnt)