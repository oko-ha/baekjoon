# https://www.acmicpc.net/problem/9996
# 이름 : 한국이 그리울 땐 서버에 접속하지
# 번호 : 9996
# 난이도 : 실버 III
# 분류 : 문자열, 브루트포스 알고리즘, 정규 표현식

import sys
import re
input = sys.stdin.readline
N = int(input())
pat = input().strip().split('*')
p = re.compile(pat[0] + '.*' + pat[1])
for _ in range(N):
    if p.sub('', input().strip()):
        print('NE')
    else:
        print('DA')