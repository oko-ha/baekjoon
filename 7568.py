# https://www.acmicpc.net/problem/7568
# 이름 : 덩치
# 번호 : 7568
# 난이도 : 실버 V
# 분류 : 

import sys
people = []
for _ in range(int(sys.stdin.readline().rstrip())):
    people.append(list(map(int, sys.stdin.readline().split())))
k = 1
n = 0
