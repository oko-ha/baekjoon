# https://www.acmicpc.net/problem/1463
# 이름 : 1로 만들기
# 번호 : 1463
# 난이도 : 실버 III
# 분류 : 다이나믹 프로그래밍

import sys
n = int(sys.stdin.readline().rstrip())
number = [0, 0, 1, 1]
for _ in range(n - 3):
    number.append(0)
for i in range(4, n + 1):
    number[i] = number[i-1] + 1
    if i % 2 == 0 and number[i//2] + 1 < number[i]:
        number[i] = number[i//2] + 1
    if i % 3 == 0 and number[i//3] + 1 < number[i]:
        number[i] = number[i//3] + 1
print(number[n])