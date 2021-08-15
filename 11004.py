# https://www.acmicpc.net/problem/11004
# 이름 : K번째 수
# 번호 : 11004
# 난이도 : 실버 V
# 분류 : 정렬

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
print(sorted(list(map(int, input().split())))[K - 1])