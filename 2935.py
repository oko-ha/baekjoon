# https://www.acmicpc.net/problem/2935
# 이름 : 소음
# 번호 : 2935
# 난이도 : 브론즈 III
# 분류 : 수학, 문자열, 사칙연산

import sys
arr = []
for _ in range(3):
    arr.append(sys.stdin.readline().rstrip())
print(eval(''.join(arr)))