# https://www.acmicpc.net/problem/2480
# 이름 : 주사위 세개
# 번호 : 2480
# 난이도 : 브론즈 IV
# 분류 : 수학, 사칙연산

import sys
a, b, c = map(int, sys.stdin.readline().split())
if a == b == c:
    print(10000 + a * 1000)
elif a != b and a != c and b != c:
    print(max(a, b, c) * 100)
else:
    if a == b or a == c:
        print(1000 + a * 100)
    else:
        print(1000 + b * 100)