# https://www.acmicpc.net/problem/8958
# 이름 : OX퀴즈
# 번호 : 8958
# 난이도 : 브론즈 II
# 분류 : 구현, 문자열

ans = []
n = int(input())
for i in range(n):
    s = input()
    sum = 0
    p = 1
    for j in s:
        if j == 'O':
            sum += p
            p += 1
        else:
            p = 1
    ans.append(sum)
for i in ans:
    print(i)