# https://www.acmicpc.net/problem/7567
# 이름 : 그릇
# 번호 : 7567
# 난이도 : 브론즈 II
# 분류 : 구현, 문자열

import sys
n = list(sys.stdin.readline().rstrip())
ans = 10
for i in range(1, len(n)):
    if n[i] == n[i - 1]:
        ans += 5
    else:
        ans += 10
print(ans)