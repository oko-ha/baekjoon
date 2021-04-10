# https://www.acmicpc.net/problem/1021
# 이름 : 회전하는 큐
# 번호 : 1021
# 난이도 : 실버 IV
# 분류 : 자료 구조, 덱

import sys
from collections import deque
from copy import deepcopy
n, m = map(int, sys.stdin.readline().split())
deq1 = deque([i for i in range(1, n+1)])
deq2 = deepcopy(deq1)
numbers = list(map(int, sys.stdin.readline().split()))
index = 0
ans = 0
while True:
    if deq1[0] == numbers[index]:
        index += 1
        deq1.popleft()
        deq2 = deepcopy(deq1)
    elif deq2[0] == numbers[index]:
        index += 1
        deq2.popleft()
        deq1 = deepcopy(deq2)
    else:
        ans += 1
        deq1.rotate()
        deq2.rotate(-1)
    if index == m:
        break
print(ans)