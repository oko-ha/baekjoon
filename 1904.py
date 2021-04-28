# https://www.acmicpc.net/problem/1904
# 이름 : 01타일
# 번호 : 1904
# 난이도 : 실버 III
# 분류 : 다이나믹 프로그래밍

import sys
n = int(sys.stdin.readline().rstrip())
a, b = 1, 2
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    i = 2
    while i < n:
        i += 1
        temp = a + b
        a = b
        b = temp % 15746
    print(b)