# https://www.acmicpc.net/problem/15700
# 이름 : 타일 채우기 4
# 번호 : 15700
# 난이도 : 브론즈 IV
# 분류 : 수학, 사칙연산

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
print(N * M // 2)