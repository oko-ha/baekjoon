# https://www.acmicpc.net/problem/9660
# 이름 : 돌 게임 6
# 번호 : 9660
# 난이도 : 골드 II
# 분류 : 수학, 게임 이론

import sys
input = sys.stdin.readline

N = int(input())
arr = [1, 0, 1, 1, 0]
print('SK' if arr[(N - 1) % len(arr)] else 'CY')