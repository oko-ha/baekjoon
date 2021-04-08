# https://www.acmicpc.net/problem/10250
# 이름 : ACM 호텔
# 번호 : 10250
# 난이도 : 브론즈 III
# 분류 : 수학, 구현, 사칙연산

import math
for _ in range(int(input())):
    h, w, n = map(int, input().split())
    if n % h != 0:
        y = str(n % h)
    else:
        y = str(h)
    print(y + str(math.ceil(n / h)).zfill(2))