# https://www.acmicpc.net/problem/11062
# 이름 : 카드 게임
# 번호 : 11062
# 난이도 : 골드 III
# 분류 : 다이나믹 프로그래밍, 게임 이론

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [[0] * N for _ in range(N)]
    def game(x, y, turn):
        if y - x < 0:
            return 0
        if dp[x][y]:
            return dp[x][y]
        if turn:
            dp[x][y] = max(game(x, y - 1, not turn) + arr[y], game(x + 1, y, not turn) + arr[x])
            return dp[x][y]
        else:
            dp[x][y] = min(game(x, y - 1, not turn), game(x + 1, y, not turn))
            return dp[x][y]
    print(game(0, N - 1, True))