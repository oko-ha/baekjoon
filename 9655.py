# https://www.acmicpc.net/problem/9655
# 이름 : 돌 게임
# 번호 : 9655
# 난이도 : 실버 V
# 분류 : 수학, 다이나믹 프로그래밍, 게임 이론

import sys
input = sys.stdin.readline

N = int(input())
print('CY' if N % 2 == 0 else 'SK')