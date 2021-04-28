# https://www.acmicpc.net/problem/1436
# 이름 : 영화감독 숌
# 번호 : 1436
# 난이도 : 실버 V
# 분류 : 브루트포스 알고리즘

import sys
n = int(sys.stdin.readline().rstrip())
number = 0
i = 0

while i < n:
    flag = True
    for k in range(3, 0, -1):
        if number % 10**k == int('6'*k):
            m = 0
            while m < 10**k:
                ans = str(number) + '6' * (3-k) + str(m).zfill(k)
                m += 1
                i += 1
                if i >= n:
                    break
            flag = False
            number += 1
            break
    if flag:
        ans = int(str(number) + '666')
        number += 1
        i += 1
print(ans)

# n = int(input())
# cnt = 0
# six_n = 666
# while True:
#     if '666' in str(six_n):
#         cnt += 1
#     if cnt == n:
#         print(six_n)
#         break
#     six_n += 1