# https://www.acmicpc.net/problem/16953
# 이름 : A → B
# 번호 : 16953
# 난이도 : 실버 I
# 분류 : 그래프 이론, 그리디 알고리즘, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

A, B = map(int, input().split())

def bfs():
    queue = deque([(A, 0)])
    while queue:
        x, cnt = queue.popleft()
        if x == B:
            return cnt + 1
        elif x < B:
            queue.append((x * 2, cnt + 1))
            queue.append((x * 10 + 1, cnt + 1))
    return -1

print(bfs())