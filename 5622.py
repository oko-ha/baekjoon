# 다이얼
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