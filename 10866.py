# https://www.acmicpc.net/problem/10866
# 이름 : 덱
# 번호 : 10866
# 난이도 : 실버 IV
# 분류 : 자료 구조, 덱

import sys
from collections import deque
deq = deque()
for _ in range(int(sys.stdin.readline().rstrip())):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push_front':
        deq.appendleft(order[1])
    elif order[0] == 'push_back':
        deq.append(order[1])
    elif order[0] == 'pop_front':
        try:
            print(deq.popleft())
        except:
            print(-1)
    elif order[0] == 'pop_back':
        try:
            print(deq.pop())
        except:
            print(-1)
    elif order[0] == 'size':
        print(len(deq))
    elif order[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        try:
            print(deq[0])
        except:
            print(-1)
    elif order[0] == 'back':
        try:
            print(deq[-1])
        except:
            print(-1)