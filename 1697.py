# https://www.acmicpc.net/problem/1697
# 이름 : 숨바꼭질
# 번호 : 1697
# 난이도 : 실버 I
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
queue = deque([(n, 0)])
visit = set()
while queue:
    d, t = queue.popleft()
    if d not in visit:
        visit.add(d)   
        if d == k:
            print(t)
            break
        else:
            next = [d - 1, d + 1, d * 2]
            for i in next:
                if 0 <= i <= 100000:
                    queue.append((i, t + 1))