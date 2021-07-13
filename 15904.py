# https://www.acmicpc.net/problem/15904
# 이름 : UCPC는 무엇의 약자일까?
# 번호 : 15904
# 난이도 : 실버 V
# 분류 : 문자열, 그리디 알고리즘

import sys
def UCPC():
    check = ['U', 'C', 'P', 'C']
    ans = ''
    for s in sys.stdin.readline().rstrip():
        if s == check[len(ans)]:
            ans += s
        if ans == 'UCPC':
            return 'I love UCPC'
    return 'I hate UCPC'
print(UCPC())