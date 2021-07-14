# https://www.acmicpc.net/problem/2636
# 이름 : 치즈
# 번호 : 2636
# 난이도 : 골드 V
# 분류 : 구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 시뮬레이션

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]
def bfs():
    queue = deque([(0, 0)])
    visit = set()
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    cnt = 0
    while queue:
        nx, ny = queue.popleft()
        if (nx, ny) not in visit:
            visit.add((nx, ny))
            if cheese[nx][ny] > 0:
                cheese[nx][ny] = 0
                cnt += 1
                continue
            for i in range(4):
                x, y = nx + dx[i], ny + dy[i]
                if 0 <= x < n and 0 <= y < m:
                    queue.append((x, y))
    return cnt
hour = 0
ans = 0
while True:
    temp = bfs()
    if temp == 0:
        break
    ans = temp
    hour += 1
print('{}\n{}'.format(hour, ans))