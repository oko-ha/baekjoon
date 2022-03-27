# https://www.acmicpc.net/problem/1032
# 이름 : 명령 프롬프트
# 번호 : 1032
# 난이도 : 브론즈 I
# 분류 : 구현, 문자열

import sys
input = sys.stdin.readline

N = int(input())
s1 = list(input().strip())
for _ in range(N - 1):
    s2 = list(input().strip())
    for i in range(len(s2)):
        if s1[i] != s2[i]:
            s1[i] = '?'
print(''.join(s1))