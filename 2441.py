# https://www.acmicpc.net/problem/2441
# 이름 : 별 찍기 - 4
# 번호 : 2441
# 난이도 : 브론즈 III
# 분류 : 구현

import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    print(' ' * i + '*' * (n - i))