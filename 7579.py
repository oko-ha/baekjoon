# https://www.acmicpc.net/problem/7579
# 이름 : 앱
# 번호 : 7579
# 난이도 : 골드 III
# 분류 : 다이나믹 프로그래밍, 배낭 문제

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
app = [0] + list(map(int, input().split()))
memory = [0] + list(map(int, input().split()))
dp = [[0] * (N + 1) for _ in range(sum(memory) + 1)]
ans = sum(memory)
for i in range(1, sum(memory) + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i][j - 1]
        if i >= memory[j]:
            dp[i][j] = max(dp[i][j], dp[i - memory[j]][j - 1] + app[j])
        if dp[i][j] >= M and ans > i:
            ans = i
print(ans)