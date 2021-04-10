# https://www.acmicpc.net/problem/5430
# 이름 : AC
# 번호 : 5430
# 난이도 : 실버 II
# 분류 : 구현, 자료 구조, 문자열, 덱

import sys
import re
from collections import deque
for _ in range(int(sys.stdin.readline().rstrip())):
    order = re.findall('\w', sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    deq = deque(re.findall('\d+', sys.stdin.readline().rstrip()))
    errFlag = False
    rotation = False
    for o in order:
        if o == 'R':
            rotation = not rotation
        else:
            if n == 0:
                errFlag = True
                break
            else:
                if rotation:
                    deq.pop()
                else:
                    deq.popleft()
                n -= 1
    if errFlag:
        print('error')
    else:
        if rotation:
            stack = []
            while len(deq) > 0:
                stack.append(deq.popleft())
            while stack:
                deq.append(stack.pop())
        print('[', end='')
        print(','.join(deq), end='')
        print(']')