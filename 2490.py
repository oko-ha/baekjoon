# https://www.acmicpc.net/problem/2490
# 이름 : 윷놀이
# 번호 : 2490
# 난이도 : 브론즈 III
# 분류 : 구현

import sys
arr = ['D', 'C', 'B', 'A', 'E']
for _ in range(3):
    print(arr[sum(map(int, sys.stdin.readline().split()))])