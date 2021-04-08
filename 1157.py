# https://www.acmicpc.net/problem/1157
# 이름 : 단어 공부
# 번호 : 1157
# 난이도 : 브론즈 I
# 분류 : 구현, 문자열

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