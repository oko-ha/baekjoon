# https://www.acmicpc.net/problem/10833
# 이름 : 사과
# 번호 : 10833
# 난이도 : 브론즈 III
# 분류 : 수학, 사칙연산

import sys
input = sys.stdin.readline
ans = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    ans += b % a
print(ans)