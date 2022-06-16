# https://www.acmicpc.net/problem/12886
# 이름 : 돌 그룹
# 번호 : 12886
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

A, B, C = map(int, input().split())

def move(x, y):
    if x > y:
        return (x - y, y + y)
    else:
        return (x + x, y - x)


def bfs():
    queue = deque([(A, B, C)])
    visit = set()
    while queue:
        a, b, c = queue.popleft()
        if (a, b, c) not in visit:
            visit.add((a, b, c))
            if a == b == c:
                return 1
            if a != b:
                queue.append(move(a, b) + (c,))
            if a != c:
                queue.append(move(a, c) + (b,))
            if b != c:
                queue.append((a,) + move(b, c))
    return 0

print(bfs())