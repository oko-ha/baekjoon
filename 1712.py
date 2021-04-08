# https://www.acmicpc.net/problem/1712
# 이름 : 손익분기점
# 번호 : 1712
# 난이도 : 브론즈 IV
# 분류 : 수학

a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    print(a // (c - b) + 1)