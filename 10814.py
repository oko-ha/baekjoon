# https://www.acmicpc.net/problem/10814
# 이름 : 나이순 정렬
# 번호 : 10814
# 난이도 : 실버 V
# 분류 : 정렬

import sys
member = []
index = 0
for _ in range(int(sys.stdin.readline().rstrip())):
    age, name = sys.stdin.readline().split()
    member.append([int(age), name, index])
    index += 1
member = sorted(member, key=lambda x : [x[0], x[2]])
for a, n, _ in member:
    print(a, n)