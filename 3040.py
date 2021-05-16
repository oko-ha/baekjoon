# https://www.acmicpc.net/problem/3040
# 이름 : 백설 공주와 일곱 난쟁이
# 번호 : 3040
# 난이도 : 브론즈 II
# 분류 : 브루트포스 알고리즘

import sys
from itertools import combinations
n = combinations([int(sys.stdin.readline()) for _ in range(9)], 7)
for i in n:
    if sum(i) == 100:
        print('\n'.join(map(str, i)))
        break