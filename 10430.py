# https://www.acmicpc.net/problem/10430
# 이름 : 나머지
# 번호 : 10430
# 난이도 : 브론즈 V
# 분류 : 수학, 구현, 사칙연산

a, b, c = map(int, input().split())
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)