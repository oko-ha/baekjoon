# https://www.acmicpc.net/problem/2164
# 이름 : 카드2
# 번호 : 2164
# 난이도 : 실버 IV
# 분류 : 자료 구조, 큐

import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
queue = deque([i for i in range(1, n+1)])
while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])