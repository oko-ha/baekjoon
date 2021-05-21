# https://www.acmicpc.net/problem/3036
# 이름 : 링
# 번호 : 3036
# 난이도 : 실버 III
# 분류 : 수학, 정수론, 유클리드 호제법

import sys
import math
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
for i in range(1, n):
    g = math.gcd(a[0], a[i])
    print('{}/{}'.format(a[0]//g, a[i]//g))