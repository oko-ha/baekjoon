# https://www.acmicpc.net/problem/10987
# 이름 : 모음의 개수
# 번호 : 10987
# 난이도 : 브론즈 II
# 분류 : 구현, 문자열

import sys
import re
print(len(re.sub('[^a|e|i|o|u]', '', sys.stdin.readline().strip())))