# https://www.acmicpc.net/problem/1987
# 이름 : 알파벳
# 번호 : 1987
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 그래프 탐색, 깊이 우선 탐색, 백트래킹

import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]
alpha = [1] * 26
alpha[ord(arr[0][0]) - 65] = 0
def backtracking(nx, ny, k):
    global ans
    ans = max(ans, k)
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    for i in range(4):
        x, y = nx + dx[i], ny + dy[i]
        if 0 <= x < R and 0 <= y < C:
            a = ord(arr[x][y]) - 65
            if alpha[a]:
                alpha[a] = 0
                backtracking(x, y, k + 1)
                alpha[a] = 1
ans = 1
backtracking(0, 0, 1)
print(ans)