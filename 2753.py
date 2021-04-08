# https://www.acmicpc.net/problem/2753
# 이름 : 윤년
# 번호 : 2753
# 난이도 : 브론즈 IV
# 분류 : 수학, 구현

a = int(input())

if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
    print('1')
else:
    print('0')