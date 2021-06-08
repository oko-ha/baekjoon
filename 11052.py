# https://www.acmicpc.net/problem/11052
# 이름 : 카드 구매하기
# 번호 : 11052
# 난이도 : 실버 I
# 분류 : 다이나믹 프로그래밍

import sys
input = sys.stdin.readline
n = int(input())
card = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    for j in range(1, n + 1 - i):
        card[i + j] = max(card[i + j], card[i] + card[j])
print(card[n])