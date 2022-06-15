# https://www.acmicpc.net/problem/1039
# 이름 : 교환
# 번호 : 139
# 난이도 : 골드 III
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
M = len(str(N))

def swap(num, i, j):
    temp = num[i]
    num[i] = num[j]
    num[j] = temp

answer = -1
queue = deque([(N, 0)])
visit = set()
while queue:
    num, k = queue.popleft()
    if k == K:
        answer = max(answer, num)
        continue
    num = list(str(num))
    for i in range(M - 1):
        for j in range(i + 1, M):
            if i == 0 and num[j] == '0':
                continue
            swap(num, i, j)
            x = int(''.join(num))
            if (x, k) not in visit:
                visit.add((x, k))
                queue.append((x, k + 1))
            swap(num, i, j)
print(answer)