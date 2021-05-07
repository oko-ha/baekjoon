# https://www.acmicpc.net/problem/2667
# 이름 : 단지번호붙이기
# 번호 : 2667
# 난이도 : 실버 I
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

import sys
input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

def dfs(x, y):
    global cnt
    if 0 <= x < n and 0 <= y < n:
        if graph[x][y] == 1:
            cnt += 1
            graph[x][y] = 0
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True
    return False

ans = []
cnt = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            ans.append(cnt)
            cnt = 0
print(len(ans))
ans.sort()
print('\n'.join(map(str, ans)))
            