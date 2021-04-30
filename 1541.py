# https://www.acmicpc.net/problem/1541
# 이름 : 잃어버린 괄호
# 번호 : 1541
# 난이도 : 실버 II
# 분류 : 수학, 그리디 알고리즘, 문자열, 파싱

import sys
s = sys.stdin.readline().rstrip().split('-')
for i in range(len(s)):
    temp = 0
    for j in s[i].split('+'):
        temp += int(j)
    if i == 0:
        ans = temp
    else:
        ans -= temp
print(ans)