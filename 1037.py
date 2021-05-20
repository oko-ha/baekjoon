# https://www.acmicpc.net/problem/1037
# 이름 : 약수
# 번호 : 1037
# 난이도 : 실버 V
# 분류 : 수학, 정수론

import sys
input = sys.stdin.readline
input()
arr = list(map(int, input().split()))
print(max(arr) * min(arr))