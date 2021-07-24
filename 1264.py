# https://www.acmicpc.net/problem/1264
# 이름 : 모음의 개수
# 번호 : 1264
# 난이도 : 브론즈 II
# 분류 : 구현, 문자열

import sys
import re
input = sys.stdin.readline
while True:
    S = input().rstrip('\n')
    if S == '#':
        break
    print(len(re.findall('a|e|i|o|u|A|E|I|O|U', S)))