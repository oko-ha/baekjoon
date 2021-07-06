# https://www.acmicpc.net/problem/16120
# 이름 : PPAP
# 번호 : 16120
# 난이도 : 골드 IV
# 분류 : 자료 구조, 그리디 알고리즘, 스택

import sys
def ppap():
    s = sys.stdin.readline().rstrip()
    p = a = 0
    for i in range(len(s)):
        if s[i] == 'P':
            if a == 1:
                a -= 1
            p += 1
        elif s[i] == 'A':
            if p < 2 or a > 0:
                return 'NP'
            else:
                p -= 2
                a += 1
    if p != 1 or a > 0:
        return 'NP'
    else:
        return 'PPAP'
print(ppap())