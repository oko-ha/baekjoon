# https://www.acmicpc.net/problem/3053
# 이름 : 택시 기하학
# 번호 : 3053
# 난이도 : 브론즈 III
# 분류 : 수학, 기하학

import sys
import math
r = float(sys.stdin.readline())
print('{:.6f}\n{:.6f}'.format(r**2*math.pi, r**2*2))