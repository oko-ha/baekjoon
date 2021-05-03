# https://www.acmicpc.net/problem/2442
# 이름 : 별 찍기 - 5
# 번호 : 2442
# 난이도 : 브론즈 III
# 분류 : 구현

import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    print(' ' * (n - i - 1) + '*' + '**' * i)