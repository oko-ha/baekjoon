# https://www.acmicpc.net/problem/18235
# 이름 : 지금 만나러 갑니다
# 번호 : 18235
# 난이도 : 골드 III
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

N, A, B = map(int, input().split())

def bfs():
    queue = deque([(A, 0, 5), (B, 0, 6)])
    visit = [0] * (N + 1)
    while queue:
        nx, k, ri = queue.popleft()
        for dx in [2 ** k, -2 ** k]:
            x = nx + dx
            if 0 < x < N + 1:
                if ri == 5:
                    visit[x] = k + 1
                elif ri == 6 and visit[x] == k + 1:
                    return k + 1
                queue.append((x, k + 1, ri))
    return -1

print(bfs())