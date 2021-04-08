from collections import Counter
n = input().upper()
h = Counter(n)
v = sorted(list(h.items()), key= lambda s: s[1], reverse=True)
try:
    if v[0][1] == v[1][1]:
        print('?')
    else:
        print(v[0][0])
except:
    print(v[0][0])