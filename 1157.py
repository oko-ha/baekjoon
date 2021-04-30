# https://www.acmicpc.net/problem/1157
# 이름 : 단어 공부
# 번호 : 1157
# 난이도 : 브론즈 I
# 분류 : 구현, 문자열

from collections import Counter
s = list(Counter(input().upper()).items())
v = sorted(s, key=lambda x:x[1], reverse=True)
if len(v) == 1 or v[0][1] != v[1][1]:
    print(v[0][0])
else:
    print('?')