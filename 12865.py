# https://www.acmicpc.net/problem/12865
# 이름 : 평범한 배낭
# 번호 : 12865
# 난이도 : 골드 V
# 분류 : 

import sys
import math
n, k = map(int, sys.stdin.readline().split())
items = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
value = [0 for _ in range(k+1)]
for item in items:
    if item[0] < k + 1:
        if value[item[0]] < item[1]:
            value[item[0]] = item[1]

# https://gsmesie692.tistory.com/113