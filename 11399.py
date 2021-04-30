# https://www.acmicpc.net/problem/11399
# 이름 : ATM
# 번호 : 11399
# 난이도 : 실버 III
# 분류 : 그리디 알고리즘, 정렬

import sys
n = int(sys.stdin.readline().rstrip())
p = sorted(list(map(int, sys.stdin.readline().split())))
for i in range(1, n):
    p[i] += p[i - 1]
print(sum(p))