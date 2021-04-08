# https://www.acmicpc.net/problem/5622
# 이름 : 다이얼
# 번호 : 5622
# 난이도 : 브론즈 II
# 분류 : 구현

h = {}
i = 65
n = 3
for _ in range(5):
    for _ in range(3):
        h[chr(i)] = n
        i += 1
    n += 1
for _ in range(4):
    h[chr(i)] = n
    i += 1
n += 1
for _ in range(3):
    h[chr(i)] = n
    i += 1
n += 1
for _ in range(4):
    h[chr(i)] = n
    i += 1

sum = 0
s = input()
for i in s:
    sum += h[i]
print(sum)