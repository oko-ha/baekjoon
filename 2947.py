# https://www.acmicpc.net/problem/2947
# 이름 : 나무조각
# 번호 : 2947
# 난이도 : 실버 V
# 분류 : 구현, 시뮬레이션

import sys
arr = list(map(int, sys.stdin.readline().split()))
while True:
    for i in range(4):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            print(*arr)
    if arr == [1, 2, 3, 4, 5]:
        break