# https://www.acmicpc.net/problem/2565
# 이름 : 전깃줄
# 번호 : 2565
# 난이도 : 실버 I
# 분류 : 다이나믹 프로그래밍

import sys
n = int(sys.stdin.readline().rstrip())
wire = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
wire = sorted(wire, key=lambda x:x[0])
ans = [1 for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        if wire[i][1] < wire[j][1]:
            if ans[i] + 1 > ans[j]:
                ans[j] = ans[i] + 1
print(n - max(ans))