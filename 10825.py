# https://www.acmicpc.net/problem/10825
# 이름 : 국영수
# 번호 : 10825
# 난이도 : 실버 IV
# 분류 : 정렬

import sys
input = sys.stdin.readline
arr = []
for _ in range(int(input())):
    a, b, c, d = input().split()
    arr.append((a, int(b), int(c), int(d)))
for name in sorted(arr, key=lambda x: (-x[1], x[2], -x[3], x[0])):
    print(name[0])