# https://www.acmicpc.net/problem/1427
# 이름 : 소트인사이드
# 번호 : 1427
# 난이도 : 실버 V
# 분류 : 문자열, 정렬

import sys
print(''.join(sorted(list(sys.stdin.readline().rstrip()), reverse=True)))