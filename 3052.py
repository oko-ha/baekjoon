from collections import Counter
num = []
for i in range(10):
    num.append(int(input()) % 42)

print(len(Counter(num)))