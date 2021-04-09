# https://www.acmicpc.net/problem/1021
# 이름 : 회전하는 큐
# 번호 : 1021
# 난이도 : 실버 IV
# 분류 : 

import sys
from collections import deque
n, i = map(int, sys.stdin.readline().split())
deq = deque([d for d in range(1, n+1)])
dic = dict.fromkeys(list(map(int, sys.stdin.readline().split())))
index = 0
ans = 0
while True:
    if deq[0] in dic:
        index += 1
    else:
        
    if index == i:
        break
print(ans)