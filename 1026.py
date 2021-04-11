# https://www.acmicpc.net/problem/1026
# 이름 : 보물
# 번호 : 1026
# 난이도 : 실버 IV
# 분류 : 정렬

from sys import stdin
n = int(stdin.readline().rstrip())
arrA = sorted(list(map(int, stdin.readline().split())))
arrB = sorted(list(map(int, stdin.readline().split())), reverse=True)
sum = 0
for a, b in zip(arrA, arrB):
    sum += a * b
print(sum)