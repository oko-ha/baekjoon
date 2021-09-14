# https://www.acmicpc.net/problem/15684
# 이름 : 사다리 조작
# 번호 : 15684
# 난이도 : 골드 IV
# 분류 : 구현, 브루트포스 알고리즘, 백트래킹

import sys
input = sys.stdin.readline
N, M, H = map(int, input().split())
arr = [[0] * N for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 1
    arr[a - 1][b] = 2
def check():
    for i in range(N):
        pos = i
        for j in range(H):
            if arr[j][pos] == 1:
                pos += 1
            elif arr[j][pos] == 2:
                pos -= 1
        if pos != i:
            return False
    return True
def dfs(k, x):
    global ans
    if check():
        ans = min(ans, k)
    if k < 3:
        for i in range(x, H):
            for j in range(N - 1):
                if arr[i][j] < 1 and arr[i][j + 1] < 1:
                    arr[i][j] = 1
                    arr[i][j + 1] = 2
                    dfs(k + 1, i)
                    arr[i][j] = 0
                    arr[i][j + 1] = 0
ans = 4
dfs(0, 0)
print(ans if ans < 4 else -1)