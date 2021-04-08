# https://www.acmicpc.net/problem/9498
# 이름 : 시험 성적
# 번호 : 9498
# 난이도 : 브론즈 IV
# 분류 : 구현

a = int(input())

if a >= 90:
    print('A')
elif a >= 80:
    print('B')
elif a >= 70:
    print('C')
elif a >= 60:
    print('D')
else:
    print('F')