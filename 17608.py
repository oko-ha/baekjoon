# https://www.acmicpc.net/problem/17608
# 이름 : 막대기
# 번호 : 17608
# 난이도 : 브론즈 II
# 분류 : 구현, 자료 구조, 스택

import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
arr.reverse()
ans = m = 0
for a in arr:
    if a > m:
        m = a
        ans += 1
print(ans)