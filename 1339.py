# https://www.acmicpc.net/problem/1339
# 이름 : 단어 수학
# 번호 : 1339
# 난이도 : 골드 IV
# 분류 : 그리디 알고리즘, 브루트포스 알고리즘

import sys
input = sys.stdin.readline

dic = {}
arr = [0] * 10
index = 0
for _ in range(int(input())):
    S = input().strip()
    for i, s in enumerate(S):
        if s not in dic:
            dic[s] = index
            index += 1
        arr[dic[s]] += 10 ** (len(S) - i - 1)
num = 0
ans = 0
for a in sorted(arr):
    ans += num * a
    num += 1
print(ans)