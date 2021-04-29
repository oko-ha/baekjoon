# https://www.acmicpc.net/problem/2156
# 이름 : 포도주 시식
# 번호 : 2156
# 난이도 : 실버 I
# 분류 : 다이나믹 프로그래밍

import sys
n = int(sys.stdin.readline().rstrip())
first = int(sys.stdin.readline().rstrip())
wine = [int(sys.stdin.readline().strip()) for _ in range(n-1)]
m = [0, 0, first, first]
for i in range(n - 1):
    m.append(m[2+4*i])
    m.append(m[3+4*i])
    m.append(m[3+4*i] + wine[i])
    m.append(max(m[:-5]) + wine[i])
print(max(m))