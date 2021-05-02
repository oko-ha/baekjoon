# https://www.acmicpc.net/problem/1212
# 이름 : 8진수 2진수
# 번호 : 1212
# 난이도 : 브론즈 IV
# 분류 : 수학, 구현, 문자열

import sys
print(bin(int(sys.stdin.readline().rstrip(), 8))[2:])