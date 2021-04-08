# https://www.acmicpc.net/problem/1330
# 이름 : 두 수 비교하기
# 번호 : 1330
# 난이도 : 브론즈 IV
# 분류 : 수학, 구현, 사칙연산

a, b = map(int, input().split())

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')