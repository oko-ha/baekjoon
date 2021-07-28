# https://www.acmicpc.net/problem/1598
# 이름 : 꼬리를 무는 숫자 나열
# 번호 : 1598
# 난이도 : 브론즈 III
# 분류 : 

import sys
a, b = map(int, sys.stdin.readline().split())
print(abs((b - 1) // 4 - (a - 1) // 4) + abs((b - 1) % 4 - (a - 1) % 4))