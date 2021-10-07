# https://www.acmicpc.net/problem/2870
# 이름 : 수학숙제
# 번호 : 2870
# 난이도 : 실버 IV
# 분류 : 문자열, 정렬

import sys
import re
input = sys.stdin.readline
arr = []
for _ in range(int(input())):
    arr += list(map(int, re.findall('\d+', input().strip())))
for a in sorted(arr):
    print(a)