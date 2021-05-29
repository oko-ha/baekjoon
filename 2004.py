# https://www.acmicpc.net/problem/2004
# 이름 : 조합 0의 개수
# 번호 : 2004
# 난이도 : 실버 II
# 분류 : 수학, 정수론

import sys
n, m = map(int, sys.stdin.readline().split())
def Counting(x, y):
    cnt = 0
    while x > 0:
        x //= y
        cnt += x
    return cnt
if m == 0:
    print(0)
else:
    two = Counting(n, 2) - Counting(m, 2) - Counting(n - m, 2)
    five = Counting(n, 5) - Counting(m, 5) - Counting(n - m, 5)
    print(min(two, five))