# https://www.acmicpc.net/problem/1546
# 이름 : 평균
# 번호 : 1546
# 난이도 : 브론즈 I
# 분류 : 수학, 사칙연산

input()
lst = list(map(int, input().split()))
m = max(lst)
sum = 0
for i in lst:
    sum += i / m * 100
print(sum/len(lst))