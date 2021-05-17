# https://www.acmicpc.net/problem/10815
# 이름 : 숫자 카드
# 번호 : 10815
# 난이도 : 실버 IV
# 분류 : 정렬, 이분 탐색

import sys
input = sys.stdin.readline
input()
d = set(map(int, input().split()))
input()
for n in list(map(int, input().split())):
    if n in d:
        print('1', end=' ')
    else:
        print('0', end=' ')