# https://www.acmicpc.net/problem/9205
# 이름 : 맥주 마시면서 걸어가기
# 번호 : 9205
# 난이도 : 실버 I
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    Sx, Sy = map(int, input().split())
    store = []
    for _ in range(n):
        x, y = map(int, input().split())
        store.append((x, y))
    Ex, Ey = map(int, input().split())
    visit = [0] * n

    def bfs():
        queue = deque([(Sx, Sy)])
        while queue:
            nx, ny = queue.popleft()
            if abs(nx - Ex) + abs(ny - Ey) <= 1000:
                return 'happy'
            for i in range(n):
                cx, cy = store[i]
                if not visit[i] and abs(nx - cx) + abs(ny - cy) <= 1000:
                    visit[i] = 1
                    queue.append((cx, cy))
        return 'sad'

    print(bfs())