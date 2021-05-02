# https://www.acmicpc.net/problem/1009
# 이름 : 분산처리
# 번호 : 1009
# 난이도 : 브론즈 III
# 분류 : 수학, 구현

import sys
n = [[10], [1], [6, 2, 4, 8], [1, 3, 9, 7], [6, 4], [5], [6], [1, 7, 9, 3], [6, 8, 4, 2], [1, 9]]
for _ in range(int(sys.stdin.readline().rstrip())):
    a, b = map(int, sys.stdin.readline().split())
    a %= 10
    b %= len(n[a])
    print(n[a][b])