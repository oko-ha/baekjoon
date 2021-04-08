# ACM 호텔
import math
for _ in range(int(input())):
    h, w, n = map(int, input().split())
    if n % h != 0:
        y = str(n % h)
    else:
        y = str(h)
    print(y + str(math.ceil(n / h)).zfill(2))