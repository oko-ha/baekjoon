# https://www.acmicpc.net/problem/2884
# 이름 : 알람 시계
# 번호 : 2884
# 난이도 : 브론즈 III
# 분류 : 수학, 사칙연산

h, m = map(int, input().split())
m -= 45
if m < 0:
    h -= 1
    m += 60
    if h < 0:
        h += 24
print(h, m)