# https://www.acmicpc.net/problem/5014
# 이름 : 스타트링크
# 번호 : 5014
# 난이도 : 골드 V
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
F, S, G, U, D = map(int, sys.stdin.readline().split())
def bfs():
    queue = deque([(S, 0)])
    visit = set()
    while queue:
        n, cnt = queue.popleft()
        if n == G:
            return cnt
        if n not in visit:
            visit.add(n)
            if F >= n + U:
                queue.append((n + U, cnt + 1))
            if 1 <= n - D:
                queue.append((n - D, cnt + 1))
    return "use the stairs"
print(bfs())