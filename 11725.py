# https://www.acmicpc.net/problem/11725
# 이름 : 트리의 부모 찾기
# 번호 : 11725
# 난이도 : 실버 II
# 분류 : 그래프 이론, 그래프 탐색, 트리, 너비 우선 탐색, 깊이 우선 탐색

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
ans = [0] * (N + 1)
def dfs(start):
    for i in graph[start]:
        if ans[i] == 0:
            ans[i] = start
            dfs(i)
dfs(1)
for a in ans[2:]:
    print(a)