# https://www.acmicpc.net/problem/9660
# 이름 : 돌 게임 6
# 번호 : 9660
# 난이도 : 골드 V
# 분류 : 게임 이론

import sys
input = sys.stdin.readline

N = int(input())
arr = [0, 1, 0, 1, 1, 1, 1]
print('SK' if arr[N % len(arr)] else 'CY')