# https://www.acmicpc.net/problem/11053
# 이름 : 가장 긴 증가하는 부분 수열
# 번호 : 11053
# 난이도 : 실버 II
# 분류 : 다이나믹 프로그래밍

import sys
n = int(sys.stdin.readline().rstrip())
number = list(map(int, sys.stdin.readline().split()))
ans = [1 for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        if number[i] < number[j]:
            if ans[i] + 1 > ans[j]:
                ans[j] = ans[i] + 1
print(max(ans))