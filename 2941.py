# https://www.acmicpc.net/problem/2941
# 이름 : 크로아티아 알파벳
# 번호 : 2941
# 난이도 : 실버 V
# 분류 : 구현, 문자열

import re
a = input()
s = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in s:
    a = re.sub(i, '!', a)
print(len(a))