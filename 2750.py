# https://www.acmicpc.net/problem/2750
# 이름 : 수 정렬하기
# 번호 : 2750
# 난이도 : 브론즈 I
# 분류 : 구현, 정렬

import sys
lst = []
for _ in range(int(sys.stdin.readline().rstrip())):
    lst.append(int(sys.stdin.readline().rstrip()))
lst.sort()
for l in lst:
    print(l)