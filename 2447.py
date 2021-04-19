# https://www.acmicpc.net/problem/2447
# 이름 : 별 찍기 - 10
# 번호 : 2447
# 난이도 : 실버 I
# 분류 : 분할 정복, 재귀

import sys
n = int(sys.stdin.readline().rstrip())
def stars(n):
    if n < 3:
        return ['*']
    n //= 3
    x = stars(n)
    top_bot = [''.join(i) for i in zip(x, x, x)]
    mid = [''.join(i) for i in zip(x, [' '*n]*n, x)]
    return top_bot + mid + top_bot
print('\n'.join(stars(n)))