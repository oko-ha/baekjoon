# https://www.acmicpc.net/problem/1075
# 이름 : 나누기
# 번호 : 1075
# 난이도 : 브론즈 II
# 분류 : 수학

import sys
n = int(sys.stdin.readline().rstrip()[:-2]+'00')
f = int(sys.stdin.readline().rstrip())
while n % f > 0:
    n += 1
print(str(n)[-2:])