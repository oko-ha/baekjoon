# https://www.acmicpc.net/problem/2953
# 이름 : 나는 요리사다
# 번호 : 2953
# 난이도 : 브론즈 III
# 분류 : 수학, 구현, 사칙연산

import sys
ans = [0, 0]
for i in range(1, 6):
    s = sum(map(int, sys.stdin.readline().split()))
    if s > ans[1]:
        ans = [i, s]
print(*ans)