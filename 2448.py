# https://www.acmicpc.net/problem/2448
# 이름 : 별 찍기 - 11
# 번호 : 2448
# 난이도 : 골드 IV
# 분류 : 재귀

import sys
n = int(sys.stdin.readline().rstrip())
def stars(k):
    if k <= 3:
        return ['  *  ', ' * * ', '*****']
    k //= 2
    x = stars(k)
    top = [''.join(i) for i in zip([' '*k]*k, x, [' '*k]*k)]
    left_right = [' '.join(i) for i in zip(x, x)]
    return top + left_right
print('\n'.join(stars(n)))