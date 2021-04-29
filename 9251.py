# https://www.acmicpc.net/problem/9251
# 이름 : LCS
# 번호 : 9251
# 난이도 : 골드 V
# 분류 : 다이나믹 프로그래밍

import sys
a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
lcs = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i - 1] == b[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
print(max(lcs[-1]))