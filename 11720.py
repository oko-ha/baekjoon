# https://www.acmicpc.net/problem/11720
# 이름 : 숫자의 합
# 번호 : 11720
# 난이도 : 브론즈 II
# 분류 : 수학, 문자열, 사칙연산

input()
s = input()
sum = 0
for i in s:
    sum += int(i)
print(sum)