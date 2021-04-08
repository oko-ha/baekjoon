# https://www.acmicpc.net/problem/2577
# 이름 : 숫자의 개수
# 번호 : 2577
# 난이도 : 브론즈 II
# 분류 : 수학, 문자열, 사칙연산

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
