# https://www.acmicpc.net/problem/9659
# 이름 : 돌 게임 5
# 번호 : 9659
# 난이도 : 실버 II
# 분류 : 게임 이론

import sys
input = sys.stdin.readline

N = int(input())
print('CY' if N % 2 == 0 else 'SK')