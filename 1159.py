# https://www.acmicpc.net/problem/1159
# 이름 : 농구 경기
# 번호 : 1159
# 난이도 : 브론즈 II
# 분류 : 문자열

import sys
from collections import Counter
input = sys.stdin.readline
name = []
for _ in range(int(input())):
    name.append(input()[0])
ans = []
for x, y in Counter(name).items():
    if y >= 5:
        ans.append(x)
if len(ans) == 0:
    print("PREDAJA")
else:
    ans.sort()
    print(''.join(ans))