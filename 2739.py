# https://www.acmicpc.net/problem/2739
# 이름 : 구구단
# 번호 : 2739
# 난이도 : 브론즈 III
# 분류 : 수학, 구현, 사칙연산

n = int(input())
for i in range(1, 10):
    print('{} * {} = {}'.format(n, i, n*i))