# https://www.acmicpc.net/problem/11866
# 이름 : 요세푸스 문제 0
# 번호 : 11866
# 난이도 : 실버 IV
# 분류 : 자료 구조, 큐

import sys
import re
from collections import deque
n, k = map(int, sys.stdin.readline().split())
queue = deque([i for i in range(1, n + 1)])
index = 1
ans = []
while True:
    if index == k:
        index = 1
        ans.append(queue.popleft())
    else:
        queue.append(queue.popleft())
        index += 1
    if not queue:
        break
print(re.sub('^\[(.*)\]$', '<\\1>', str(ans)))