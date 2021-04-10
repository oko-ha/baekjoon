# https://www.acmicpc.net/problem/2751
# 이름 : 수 정렬하기 2
# 번호 : 2751
# 난이도 : 실버 V
# 분류 : 정렬

import sys
lst = []
for _ in range(int(sys.stdin.readline().rstrip())):
    lst.append(int(sys.stdin.readline().rstrip()))
lst.sort()
for l in lst:
    print(l)