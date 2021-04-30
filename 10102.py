# https://www.acmicpc.net/problem/10102
# 이름 : 개표
# 번호 : 10102
# 난이도 : 브론즈 II
# 분류 : 문자열

import sys
from collections import Counter
sys.stdin.readline()
v = Counter(list(sys.stdin.readline()))
if v['A'] > v['B']: print('A')
elif v['B'] > v['A']: print('B')
else: print('Tie')