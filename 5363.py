# https://www.acmicpc.net/problem/5363
# 이름 : 요다
# 번호 : 5363
# 난이도 : 브론즈 II
# 분류 : 구현, 문자열

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    s = list(input().split())
    print(*(s[2:] + s[:2]))