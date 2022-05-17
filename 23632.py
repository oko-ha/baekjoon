# https://www.acmicpc.net/problem/23632
# 이름 : 쿠키런 킹덤
# 번호 : 23632
# 난이도 : 골드 II
# 분류 : 그래프 이론, 위상 정렬

import sys
from collections import deque
input = sys.stdin.readline

N, M, T = map(int, input().split())
queue = deque()
for i in map(int, input().split()):
    queue.append((i, 0))
res = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    arr = list(map(int, input().split()))
    res[i] += arr[1:]
bld = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(N - M):
    arr = list(map(int, input().split()))
    for i in arr[2:]:
        bld[i].append(arr[0])
    indegree[arr[0]] = arr[1]
ans = []
temp = set()
while queue:
    nx, t = queue.popleft()
    if t > T:
        continue
    ans.append(nx)
    for dx in res[nx]:
        if dx in temp:
            continue
        temp.add(dx)
        for x in bld[dx]:
            indegree[x] -= 1
            if indegree[x] == 0:
                queue.append((x, t + 1))
print(len(ans))
print(*sorted(ans))