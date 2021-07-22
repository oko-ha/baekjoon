# https://www.acmicpc.net/problem/10820
# 이름 : 문자열 분석
# 번호 : 10820
# 난이도 : 브론즈 II
# 분류 : 구현, 문자열

import sys
while True:
    s = sys.stdin.readline().rstrip('\n')
    if not s:
        break
    a = [0, 0, 0, 0]
    for i in s:
        if i.islower():
            a[0] += 1
        elif i.isupper():
            a[1] += 1
        elif i.isdigit():
            a[2] += 1
        else:
            a[3] += 1
    print(*a)