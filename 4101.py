# https://www.acmicpc.net/problem/4101
# 이름 : 크냐?
# 번호 : 4101
# 난이도 : 브론즈 III
# 분류 : 수학, 구현

import sys
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == b == 0:
        break
    if a > b:
        print("Yes")
    else:
        print("No")