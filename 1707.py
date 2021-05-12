# https://www.acmicpc.net/problem/1707
# 이름 : 이분 그래프
# 번호 : 1707
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

def bfs(i):
    queue = deque()
    check[i] = 1
    queue.append(i)
    while queue:
        n = queue.popleft()
        for a in arr[n]:
            if check[a] == 0:
                check[a] = check[n] * -1
                queue.append(a)
            elif check[a] == check[n]:
                return True
    return False

def answer():
    for i in range(1, v + 1):
        if check[i] == 0:
            if bfs(i):
                return 'NO'
    return 'YES'

for _ in range(int(input())):
    v, e = map(int, input().split())
    arr = [[] for _ in range(v + 1)]
    check = [0 for _ in range(v + 1)]
    for _ in range(e):
        x, y = map(int, input().split())
        arr[x].append(y)
        arr[y].append(x)
    print(answer())