# https://www.acmicpc.net/problem/10951
# 이름 : A+B -4
# 번호 : 10951
# 난이도 : 브론즈 III
# 분류 : 수학, 구현, 사칙연산

while True:
    try:
        print(sum(map(int, input().split())))
    except:
        break