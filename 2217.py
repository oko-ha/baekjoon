# https://www.acmicpc.net/problem/2217
# 이름 : 로프
# 번호 : 2217
# 난이도 : 실버 IV
# 분류 : 수학, 그리디 알고리즘, 정렬, 물리학

import sys
input = sys.stdin.readline
n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))
rope.sort()
ans = []
for i in range(n):
    ans.append(rope[i] * (n - i))
print(max(ans))