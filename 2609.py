# https://www.acmicpc.net/problem/2609
# 이름 : 최대공약수와 최소공배수
# 번호 : 2609
# 난이도 : 실버 V
# 분류 : 수학, 정수론, 유클리드 호제법

import sys
x, y = map(int, sys.stdin.readline().split())
cd = []
i = 1
while x >= i and y >= i:
    if x % i == 0 and y % i == 0:
        cd.append(i)
    i += 1
print(max(cd))
i = 1
while (x * i) % y != 0:
    i += 1
print(x * i)