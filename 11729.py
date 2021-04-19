# https://www.acmicpc.net/problem/11729
# 이름 : 하노이 탑 이동 순서
# 번호 :11729
# 난이도 : 실버 II
# 분류 : 재귀

import sys
n = int(sys.stdin.readline().rstrip())
def hanoi(n, x, y, z):
    if n == 1:
        print(x, z)
    else:
        hanoi(n - 1, x, z, y)
        print(x, z)
        hanoi(n - 1, y, x, z)
print(2 ** n - 1)
hanoi(n, 1, 2, 3)