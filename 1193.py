# https://www.acmicpc.net/problem/1193
# 이름 : 분수찾기
# 번호 : 1193
# 난이도 : 브론즈 II
# 분류 : 수학, 구현

n = int(input())
i = 0
s = 0
while s < n:
    i += 1
    s += i
s = s - i + 1
if i % 2 == 0:
    a, b = 1, i
else:
    a, b = i, 1
for j in range(n - s):
    if i % 2 == 0:
        a += 1
        b -= 1
    else:
        a -= 1
        b += 1
print('{}/{}'.format(a, b))