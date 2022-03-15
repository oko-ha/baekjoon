# https://www.acmicpc.net/problem/15558
# 이름 : 점프 게임
# 번호 : 15558
# 난이도 : 실버 I
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

N, k = map(int, input().split())
arr = [list(input().strip()) for _ in range(2)]
def bfs():
    arr[0][0] = '0'
    queue = deque([(0, 0, 0)])
    while queue:
        x, ny, t = queue.popleft()
        for dy in [1, -1, k]:
            if dy == k:
                x ^= 1
            y = ny + dy
            if y >= N:
                return 1
            if y > t and arr[x][y] == '1':
                arr[x][y] = '0'
                queue.append((x, y, t + 1))
    return 0
print(bfs())