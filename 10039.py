# https://www.acmicpc.net/problem/10039
# 이름 : 평균 점수
# 번호 : 10039
# 난이도 : 브론즈 IV
# 분류 : 수학, 사칙연산

import sys
s = 0
for _ in range(5):
    n = int(sys.stdin.readline())
    if n < 40: n = 40
    s += n
print(s//5)