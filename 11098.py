# https://www.acmicpc.net/problem/11098
# 이름 : 첼시를 도와줘!
# 번호 : 11098
# 난이도 : 브론즈 I
# 분류 : 구현, 문자열

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    ans, m = '', 0
    for _ in range(int(input())):
        c, n = input().split()
        if int(c) > m:
            ans, m = n, int(c)
    print(ans)