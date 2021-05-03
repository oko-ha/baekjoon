# https://www.acmicpc.net/problem/2010
# 이름 : 플러그
# 번호 : 2010
# 난이도 : 브론즈 III
# 분류 : 수학, 구현, 사칙연산

import sys
n = int(sys.stdin.readline().rstrip())
plug = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
print(sum(plug) - n + 1)