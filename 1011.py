# https://www.acmicpc.net/problem/1011
# 이름 : Fly me to the Alpha Centauri
# 번호 : 1011
# 난이도 : 실버 I
# 분류 : 수학

import sys
for _ in range(int(sys.stdin.readline().rstrip())):
    x, y = map(int, sys.stdin.readline().split())
    dist = y - x
    if dist == 1:
        print(1)
    elif dist == 2:
        print(2)
    else:
        a = 4; b = 6
        index = 2
        cnt = 3
        while True:
            if dist <= a:
                print(cnt)
                break
            elif dist <= b:
                print(cnt + 1)
                break
            cnt += 2
            index += 1
            a = b + index
            b = a + index