# https://www.acmicpc.net/problem/2033
# 이름 : 반올림
# 번호 : 2033
# 난이도 : 브론즈 I
# 분류 : 수학, 구현

import sys
n = list(map(int, sys.stdin.readline().rstrip()))
for i in range(len(n) - 1, 0, -1):
    if n[i] >= 5:
        n[i - 1] = n[i - 1] + 1
    n[i] = 0
print(''.join(map(str, n)))