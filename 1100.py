# https://www.acmicpc.net/problem/1100
# 이름 : 하얀 칸
# 번호 : 1100
# 난이도 : 브론즈 II
# 분류 : 구현, 문자열

import sys
ans = 0
for i in range(8):
    s = sys.stdin.readline().rstrip()
    for j in range(i % 2, 8, 2):
        if s[j] == 'F':
            ans += 1
print(ans)