# https://www.acmicpc.net/problem/1292
# 이름 : 쉽게 푸는 문제
# 번호 : 1292
# 난이도 : 실버 V
# 분류 : 수학, 구현

import sys
input = sys.stdin.readline
A, B = map(int, input().split())
arr = []
i = 1
while len(arr) < B:
    arr += [i] * i
    i += 1
print(sum(arr[A - 1:B]))