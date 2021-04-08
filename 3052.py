# https://www.acmicpc.net/problem/3052
# 이름 : 나머지
# 번호 : 3052
# 난이도 : 브론즈 II
# 분류 : 수학, 사칙연산

from collections import Counter
num = []
for i in range(10):
    num.append(int(input()) % 42)

print(len(Counter(num)))