# https://www.acmicpc.net/problem/2443
# 이름 : 별 찍기 - 6
# 번호 : 2443
# 난이도 : 브론즈 III
# 분류 : 구현

import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    print(' ' * i + '*' + '**' * (n - i - 1))