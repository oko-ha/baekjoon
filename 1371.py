# https://www.acmicpc.net/problem/1371
# 이름 : 가장 많은 글자
# 번호 : 1371
# 난이도 : 브론즈 II
# 분류 : 구현, 문자열

import sys
from collections import Counter
dic = Counter(sys.stdin.read()).most_common()
ans = []
m = 0
for i in range(len(dic)):
    if dic[i][0].isalpha():
        if m == 0:
            m = dic[i][1]
        if m > dic[i][1]:
            break
        else:
            ans.append(dic[i][0])
print(''.join(sorted(ans)))