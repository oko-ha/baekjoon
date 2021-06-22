# https://www.acmicpc.net/problem/1789
# 이름 : 수들의 합
# 번호 : 1789
# 난이도 : 실버 V
# 분류 : 수학, 그리디 알고리즘

import sys
s = int(sys.stdin.readline())
i = 1
while i <= s:
    s -= i
    i += 1
print(i - 1)