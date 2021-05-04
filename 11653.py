# https://www.acmicpc.net/problem/11653
# 이름 : 소인수분해
# 번호 : 11653
# 난이도 : 실버 IV
# 분류 : 수학, 정수론, 소수 판정

import sys
n = int(sys.stdin.readline())
i = 2
while n > 1:
    if n % i == 0:
        n //= i
        print(i)
    else:
        i += 1