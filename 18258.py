# https://www.acmicpc.net/problem/18258
# 이름 : 큐 2
# 번호 : 18258
# 난이도 : 실버 IV
# 분류 : 자료 구조, 큐

import sys
from collections import deque
queue = deque()
for _ in range(int(sys.stdin.readline().rstrip())):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        queue.append(order[1])
    elif order[0] == 'pop':
        try:
            print(queue.popleft())
        except:
            print(-1)
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        try:
            print(queue[0])
        except:
            print(-1)
    elif order[0] == 'back':
        try:
            print(queue[-1])
        except:
            print(-1)