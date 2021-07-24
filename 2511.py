# https://www.acmicpc.net/problem/2511
# 이름 : 카드놀이
# 번호 : 2511
# 난이도 : 브론즈 III
# 분류 : 구현

import sys
input = sys.stdin.readline
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
point = [0, 0]
winner = 'D'
for a, b in zip(arr1, arr2):
    if a > b:
        point[0] += 3
        winner = 'A'
    elif a < b:
        point[1] += 3
        winner = 'B'
    else:
        point[0] += 1
        point[1] += 1
if point[0] > point[1]:
    winner = 'A'
elif point[0] < point[1]:
    winner = 'B'
print(*point)
print(winner)