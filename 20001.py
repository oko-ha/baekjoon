# https://www.acmicpc.net/problem/20001
# 이름 : 고무오리 디버깅
# 번호 : 20001
# 난이도 : 브론즈 I
# 분류 : 구현, 자료 구조, 스택

import sys
prob = 0
while True:
    s = sys.stdin.readline().strip()
    if s == '고무오리 디버깅 끝':
        break
    if s == '문제':
        prob += 1
    elif s == '고무오리':
        if prob > 0:
            prob -= 1
        else:
            prob += 2
if prob > 0:
    print('힝구')
else:
    print('고무오리야 사랑해')