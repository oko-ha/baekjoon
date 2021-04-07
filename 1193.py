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