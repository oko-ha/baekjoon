# https://www.acmicpc.net/problem/6603
# 이름 : 로또
# 번호 : 6603
# 난이도 : 실버 II
# 분류 : 수학, 조합론, 백트래킹, 재귀

import sys
from itertools import combinations
while True:
    arr = list(map(int, sys.stdin.readline().split()))
    if arr[0] == 0:
        break
    for i in combinations(arr[1:], 6):
        print(*i)
    print()