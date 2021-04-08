# https://www.acmicpc.net/problem/9012
# 이름 : 괄호
# 번호 : 9012
# 난이도 : 실버 IV
# 분류 : 자료 구조, 문자열, 스택

from sys import stdin
from collections import Counter
for _ in range(int(stdin.readline().rstrip())):
    s = stdin.readline().rstrip()
    c = Counter(s)
    if c['('] == c[')']:
        b = [0, 0]
        ans = 'YES'
        for i in s:
            if i == '(':
                b[0] += 1
            else:
                b[1] += 1
            if b[0] - b[1] < 0:
                ans = 'NO'
                break
    else:
        ans = 'NO'
    print(ans)