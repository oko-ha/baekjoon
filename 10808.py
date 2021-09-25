# https://www.acmicpc.net/problem/10808
# 이름 : 알파벳 개수
# 번호 : 10808
# 난이도 : 브론즈 II
# 분류 : 구현, 문자열

import sys
a = [0] * 26
for i in sys.stdin.readline().strip():
    a[ord(i) - 97] += 1
print(*a)