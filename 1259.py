# https://www.acmicpc.net/problem/1259
# 이름 : 팰린드롬수
# 번호 : 1259
# 난이도 : 브론즈 I
# 분류 : 구현, 문자열

import sys
input = sys.stdin.readline
def palindrome(n):
        for i in range(len(n) // 2):
            if n[i] != n[len(n) - i - 1]:
                return "no"
        return "yes"
while True:
    n = input().strip()
    if n == '0':
        break
    print(palindrome(n))