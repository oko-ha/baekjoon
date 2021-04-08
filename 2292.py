# https://www.acmicpc.net/problem/2292
# 이름 : 벌집
# 번호 : 2292
# 난이도 : 브론즈 II
# 분류 : 수학

n = int(input())

i = 2
j = 1
while True:
    if n == 1:
        print(1)
        break
    elif n in range(i, (i + 6 * j)):
        print(j + 1)
        break
    i += 6 * j
    j += 1