# https://www.acmicpc.net/problem/14681
# 이름 : 사분면 고르기
# 번호 : 14681
# 난이도 : 브론즈 IV
# 분류 : 구현, 기하학

x = int(input())
y = int(input())
if x > 0:
    if y > 0:
        print('1')
    else:
        print('4')
else:
    if y > 0:
        print('2')
    else:
        print('3')