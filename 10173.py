# https://www.acmicpc.net/problem/10173
# 이름 : 니모를 찾아서
# 번호 : 10173
# 난이도 : 브론즈 II
# 분류 : 문자열

import sys
while True:
    s = sys.stdin.readline().rstrip()
    if s == 'EOI':
        break
    print('Found' if 'NEMO' in s.upper() else 'Missing')