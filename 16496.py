# https://www.acmicpc.net/problem/16496
# 이름 : 큰 수 만들기
# 번호 : 16496
# 난이도 : 플래티넘 V
# 분류 : 그리디 알고리즘, 정렬

import sys
from functools import cmp_to_key
input = sys.stdin.readline

N = int(input())
arr = list(input().split())
def compare(a, b):
    if int(a + b) > int(b + a):
        return -1
    elif int(a + b) < int(b + a):
        return 1
    else:
        return 0
arr = sorted(arr, key=cmp_to_key(compare))
print(int(''.join(arr)))