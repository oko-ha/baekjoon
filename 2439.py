# https://www.acmicpc.net/problem/2439
# 이름 : 별 찍기 -2
# 번호 : 2439
# 난이도 : 브론즈 III
# 분류 : 구현

n = int(input())
for i in range(n):
    print(" "*(n-i-1), end="")
    print("*"*(i+1))