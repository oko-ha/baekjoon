# https://www.acmicpc.net/problem/15922
# 이름 : 아우으 우아으이야!!
# 번호 : 15922
# 난이도 : 골드 V
# 분류 : 그리디 알고리즘, 정렬, 스위핑

import sys
input = sys.stdin.readline
ans = 0
for i in range(int(input())):
    if i == 0:
        x, y = map(int, input().split())
    if i > 0:
        a, b = map(int, input().split())
        if a <= y and b > y:
            y = b
        elif a > y:
            ans += y - x
            x, y = a, b
print(ans + (y - x))