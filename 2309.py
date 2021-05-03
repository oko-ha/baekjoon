# https://www.acmicpc.net/problem/2309
# 이름 : 일곱 난쟁이
# 번호 : 2309
# 난이도 : 브론즈 II
# 분류 : 브루트포스 알고리즘

import sys
from itertools import combinations
dwarfs = [int(sys.stdin.readline().rstrip()) for _ in range(9)]
dwarfs = list(combinations(dwarfs, 7))
ans = []
for dwarf in dwarfs:
    if sum(dwarf) == 100:
        ans = sorted(list(dwarf))
print('\n'.join(map(str, ans)))