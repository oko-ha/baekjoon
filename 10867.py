# https://www.acmicpc.net/problem/10867
# 이름 : 중복 빼고 정렬하기
# 번호 : 10867
# 난이도 : 실버 V
# 분류 : 정렬

import sys
input = sys.stdin.readline
input()
n = list(set(map(int, input().split())))
n.sort()
print(*n)