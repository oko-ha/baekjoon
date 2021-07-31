# https://www.acmicpc.net/problem/2693
# 이름 : N번째 큰 수
# 번호 : 2693
# 난이도 : 실버 V
# 분류 : 구현, 정렬

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    arr = sorted(list(map(int, input().split())), reverse=True)
    print(arr[2])