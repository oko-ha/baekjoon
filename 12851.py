# https://www.acmicpc.net/problem/12851
# 이름 : 숨바꼭질 2
# 번호 : 12851
# 난이도 : 골드 V
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
if N > K:
    print(str(N - K)+'\n1')
elif N == K:
    print('0\n1')
else:
    dp = [-1] * 100001
    dp[N] = 0
    queue = deque([N])
    ans = 0
    while queue:
        n = queue.popleft()
        if n == K:
            ans += 1
        for i in [n + 1, n - 1, n * 2] if n < K else [n - 1]:
            if 0 <= i <= 100000:
                if dp[i] == -1 or dp[i] >= dp[n] + 1:
                    dp[i] = dp[n] + 1
                    queue.append(i)
    print('{}\n{}'.format(dp[K], ans))