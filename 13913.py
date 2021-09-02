# https://www.acmicpc.net/problem/13913
# 이름 : 숨바꼭질 4
# 번호 : 13913
# 난이도 : 골드 IV
# 분류 : 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
if N > K:
    print(N - K)
    print(' '.join([str(i) for i in range(N, K-1, -1)]))
elif N == K:
    print('0\n'+str(N))
else:
    dp = [-1] * 100001
    dp[N] = 0
    queue = deque([(N, dict())])
    ans = 0
    while queue:
        n, d = queue.popleft()
        if n == K:
            print(dp[K])
            print(' '.join([str(i) for i in d.keys()] + [str(K)]))
            break
        for i in [n + 1, n - 1, n * 2] if n < K else [n - 1]:
            if 0 <= i <= 100000:
                if dp[i] == -1 or dp[i] >= dp[n] + 1:
                    dp[i] = dp[n] + 1
                    queue.append((i, {**d, **{n:i}}))