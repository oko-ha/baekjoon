from collections import Counter

a = int(input())
b = int(input())
c = int(input())
l = Counter(str(a * b * c))
for i in range(0, 10):
    try:
        print(l[str(i)])
    except:
        print('0')
