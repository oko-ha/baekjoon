# https://www.acmicpc.net/problem/1934
# 이름 : 최소공배수
# 번호 : 1934
# 난이도 : 실버 V
# 분류 : 수학, 정수론, 유클리드 호제법

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a = list(map(int, input().split()))
    x, y = max(a), min(a)
    while x % y != 0:
        x, y = y, x % y
    print((a[0] * a[1]) // y)