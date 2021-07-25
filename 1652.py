# https://www.acmicpc.net/problem/1652
# 이름 : 누울 자리를 찾아라
# 번호 : 1652
# 난이도 : 브론즈 I
# 분류 : 구현, 문자열

import sys
input = sys.stdin.readline
N = int(input())
arr = [list(input().strip()) for _ in range(N)]
x = y = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if arr[i][j] == '.':
            cnt += 1
        else:
            if cnt > 1:
                x += 1
            cnt = 0
    if cnt > 1:
        x += 1
for j in range(N):
    cnt = 0
    for i in range(N):
        if arr[i][j] == '.':
            cnt += 1
        else:
            if cnt > 1:
                y += 1
            cnt = 0
    if cnt > 1:
        y += 1
print(x, y)