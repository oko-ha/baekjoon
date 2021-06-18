# https://www.acmicpc.net/problem/10953
# 이름 : A+B -6
# 번호 : 10953
# 난이도 : 브론즈 II
# 분류 : 수학, 문자열, 사칙연산, 파싱

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    print(sum(map(int, input().split(','))))