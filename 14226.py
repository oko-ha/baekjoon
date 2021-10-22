# https://www.acmicpc.net/problem/14226
# 이름 : 이모티콘
# 번호 : 14226
# 난이도 : 골드 V
# 분류 : 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
S = int(sys.stdin.readline())
queue = deque([(1, 0)])
dp = [[-1] * (S + 1) for _ in range(S + 1)]
dp[1][0] = 0
while queue:
    x, clip = queue.popleft()
    if dp[x][x] == -1:
        dp[x][x] = dp[x][clip] + 1
        queue.append((x, x))
    if x + clip <= S and dp[x + clip][clip] == -1:
        dp[x + clip][clip] = dp[x][clip] + 1
        queue.append((x + clip, clip))
    if x - 1 > 1 and dp[x - 1][clip] == -1:
        dp[x - 1][clip] = dp[x][clip] + 1
        queue.append((x - 1, clip))
ans = float('inf')
for d in dp[S]:
    if d > 0:
        ans = min(ans, d)
print(ans)