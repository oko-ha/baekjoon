# https://www.acmicpc.net/problem/9656
# 이름 : 돌 게임 2
# 번호 : 9656
# 난이도 : 실버 IV
# 분류 : 다이나믹 프로그래밍, 게임 이론

import sys
input = sys.stdin.readline

N = int(input())
print('SK' if N % 2 == 0 else 'CY')