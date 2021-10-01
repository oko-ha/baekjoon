# https://www.acmicpc.net/problem/9019
# 이름 : DSLR
# 번호 : 9019
# 난이도 : 골드 V
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
def bfs():
    visit = [0] * 10000
    queue = deque([(A, '')])
    while queue:
        n, d = queue.popleft()
        for x, s in [(n * 2 % 10000, 'D'), ((n - 1) % 10000, 'S'), (n % 1000 * 10 + n // 1000, 'L'), (n % 10 * 1000 + n // 10, 'R')]:
            if x == B:
                return d + s
            elif visit[x] < 1:
                visit[x] = 1
                queue.append((x, d + s))
input = sys.stdin.readline
for _ in range(int(input())):
    A, B = map(int, input().split())
    print(bfs())