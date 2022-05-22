# https://www.acmicpc.net/problem/14395
# 이름 : 4연산
# 번호 : 14395
# 난이도 : 골드 V
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

s, t = map(int, input().split())

def bfs():
    queue = deque([(s, '')])
    while queue:
        x, a = queue.popleft()
        if x == t:
            return a
        if x < t:
            if x > 1:
                queue.append((x ** 2, a + '*'))
            queue.append((x * 2, a + '+'))
        if a == '':
            queue.append((1, '/'))
    return -1

if s == t:
    print(0)
elif t == 0:
    print('-')
else:
    print(bfs())