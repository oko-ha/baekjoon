# https://www.acmicpc.net/problem/12100
# 이름 : 2048 (Easy)
# 번호 : 12100
# 난이도 : 골드 II
# 분류 : 구현, 브루트포스 알고리즘, 시뮬레이션, 백트래킹

import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
def left(arr):
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        t = k = 0
        for j in range(N):
            if arr[i][j] == 0:
                continue
            if t < 1:
                t = arr[i][j]
                continue
            if arr[i][j] == t:
                temp[i][k] = t * 2
                t = 0
            else:
                temp[i][k] = t
                t = arr[i][j]
            k += 1
        if t > 1:
            temp[i][k] = t
    return temp
def right(arr):
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        t, k = 0, N - 1
        for j in range(N - 1, -1, -1):
            if arr[i][j] == 0:
                continue
            if t < 1:
                t = arr[i][j]
                continue
            if arr[i][j] == t:
                temp[i][k] = t * 2
                t = 0
            else:
                temp[i][k] = t
                t = arr[i][j]
            k -= 1
        if t > 1:
            temp[i][k] = t
    return temp
def up(arr):
    temp = [[0] * N for _ in range(N)]
    for j in range(N):
        t = k = 0
        for i in range(N):
            if arr[i][j] == 0:
                continue
            if t < 1:
                t = arr[i][j]
                continue
            if arr[i][j] == t:
                temp[k][j] = t * 2
                t = 0
            else:
                temp[k][j] = t
                t = arr[i][j]
            k += 1
        if t > 1:
            temp[k][j] = t
    return temp
def down(arr):
    temp = [[0] * N for _ in range(N)]
    for j in range(N):
        t, k = 0, N - 1
        for i in range(N - 1, -1, -1):
            if arr[i][j] == 0:
                continue
            if t < 1:
                t = arr[i][j]
                continue
            if arr[i][j] == t:
                temp[k][j] = t * 2
                t = 0
            else:
                temp[k][j] = t
                t = arr[i][j]
            k -= 1
        if t > 1:
            temp[k][j] = t
    return temp
def dfs(arr, k):
    global ans
    if k < 5:
        dfs(left(arr), k + 1)
        dfs(right(arr), k + 1)
        dfs(up(arr), k + 1)
        dfs(down(arr), k + 1)
    else:
        ans = max(ans, max(map(max, arr)))
ans = 0
dfs(arr, 0)
print(ans)