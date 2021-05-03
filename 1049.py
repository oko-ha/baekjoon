# https://www.acmicpc.net/problem/1049
# 이름 : 기타줄
# 번호 : 1049
# 난이도 : 실버 IV
# 분류 : 수학

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
minPack = minPiece = 1000
for _ in range(m):
    pack, piece = map(int, input().split())
    if pack < minPack:
        minPack = pack
    if piece < minPiece:
        minPiece = piece
if minPiece * 6 < minPack:
    print(minPiece * n)
else:
    ans = minPack * (n // 6)
    temp = n % 6
    if minPiece * temp < minPack:
        print(ans + minPiece * temp)
    else:
        print(ans + minPack)