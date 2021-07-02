# https://www.acmicpc.net/problem/2563
# 이름 : 색종이
# 번호 : 2563
# 난이도 : 실버 V
# 분류 : 구현

import sys
input = sys.stdin.readline
arr = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            arr[i][j] = 1
ans = 0
for a in arr:
    ans += sum(a)
print(ans)