# https://www.acmicpc.net/problem/1252
# 이름 : 이진수 덧셈
# 번호 : 1252
# 난이도 : 브론즈 I
# 분류 : 수학, 구현,

import sys
a, b = sys.stdin.readline().split()
print(bin(int(a, 2) + int(b, 2))[2:])