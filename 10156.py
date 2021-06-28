# https://www.acmicpc.net/problem/10156
# 이름 : 과자
# 번호 : 10156
# 난이도 : 브론즈 IV
# 분류 : 수학, 사칙연산

import sys
K, N, M = map(int, sys.stdin.readline().split())
print(K * N - M if K * N - M > 0 else 0)