# https://www.acmicpc.net/problem/1484
# 이름 : 다이어트
# 번호 : 1484
# 난이도 : 골드 IV
# 분류 : 수학, 정수론, 두 포인터

import sys
import math
input = sys.stdin.readline
ans = []
G = int(input())
for i in range(1, 50001):
    if i ** 2 > G:
        temp = math.sqrt(i ** 2 - G)
        if temp.is_integer():
            ans.append(i)
if ans:
    for a in ans:
        print(a)
else:
    print(-1)