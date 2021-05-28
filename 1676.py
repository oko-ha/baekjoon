# https://www.acmicpc.net/problem/1676
# 이름 : 팩토리얼 0의 개수
# 번호 : 1676
# 난이도 : 실버 III
# 분류 : 수학

import sys
from math import factorial
n = list(str(factorial(int(sys.stdin.readline()))))
cnt = 0
for i in range(len(n) - 1, -1, -1):
    if n[i] == '0':
        cnt += 1
    else:
        break
print(cnt)