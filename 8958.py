# OX퀴즈
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