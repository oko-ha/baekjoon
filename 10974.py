# https://www.acmicpc.net/problem/10974
# 이름 : 모든 순열
# 번호 : 10974
# 난이도 : 실버 III
# 분류 : 브루트포스 알고리즘

import sys
from itertools import permutations
n = [i for i in range(1, int(sys.stdin.readline()) + 1)]
for a in list(permutations(n, len(n))):
    print(*a)