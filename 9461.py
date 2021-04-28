# https://www.acmicpc.net/problem/9461
# 이름 : 파도반 수열
# 번호 : 9461
# 난이도 : 실버 III
# 분류 : 수학, 다이나믹 프로그래밍

import sys
for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    a, b, c = 1, 1, 1
    if n == 1:
        print(1)
    elif n == 2:
        print(1)
    elif n == 3:
        print(1)
    else:
        i = 3
        while i < n:
            i += 1
            temp = a + b
            a = b
            b = c
            c = temp
        print(c)