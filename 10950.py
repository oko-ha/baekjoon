# https://www.acmicpc.net/problem/10950
# 이름 : A+B -3
# 번호 : 10950
# 난이도 : 브론즈 III
# 분류 : 수학, 구현, 사칙연산

n = int(input())
ans = []
for i in range(n):
    ans.append(sum(map(int, input().split())))
for i in ans:
    print(i)