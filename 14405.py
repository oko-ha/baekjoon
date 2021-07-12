# https://www.acmicpc.net/problem/14405
# 이름 : 피카츄
# 번호 : 14405
# 난이도 : 실버 V
# 분류 : 문자열

import sys
import re
S = re.sub('(pi)|(ka)|(chu)', '', sys.stdin.readline().rstrip())
if len(S) > 0:
    print('NO')
else:
    print('YES')