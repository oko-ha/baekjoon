# https://www.acmicpc.net/problem/1013
# 이름 : Contact
# 번호 : 1013
# 난이도 : 골드 V
# 분류 : 문자열, 정규 표현식

import sys
import re
input = sys.stdin.readline
for _ in range(int(input())):
    if re.fullmatch('(100+1+|01)+', input().strip()):
        print("YES")
    else:
        print("NO")