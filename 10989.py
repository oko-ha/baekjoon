# https://www.acmicpc.net/problem/10989
# 이름 : 수 정렬하기 3
# 번호 : 10989
# 난이도 : 실버 V
# 분류 : 정렬

import sys
arr = [0] * 10000
for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    arr[n - 1] += 1
for i in range(len(arr)):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i + 1)