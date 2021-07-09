# https://www.acmicpc.net/problem/2457
# 이름 : 공주님의 정원
# 번호 : 2457
# 난이도 : 골드 IV
# 분류 : 그리디 알고리즘

import sys
input = sys.stdin.readline
flower = []
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a < 3:
        a, b = 3, 1
    if c > 11:
        c, d = 12, 1
    if c > 2:
        flower.append((a, b, c, d))
flower = sorted(flower, key=lambda x:(x[0], x[1]))
def gardening():
    cur_month, cur_day = 3, 1
    max_month, max_day = 3, 1
    cnt = 0
    for a, b, c, d in flower:
        if a > max_month or (a == max_month and  b > max_day):
            return 0
        if a > cur_month or (a == cur_month and  b > cur_day):
            cur_month, cur_day = max_month, max_day
            cnt += 1
        if c > max_month or (c == max_month and d > max_day):
            max_month, max_day = c, d
        if max_month == 12 and max_day == 1:
            return cnt + 1
    return 0
print(gardening())