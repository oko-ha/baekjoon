# https://www.acmicpc.net/problem/1543
# 이름 : 문서 검색
# 번호 : 1543
# 난이도 : 실버 IV
# 분류 : 문자열, 그리디 알고리즘, 브루트포스 알고리즘

import sys
input = sys.stdin.readline
S = input().rstrip()
s = input().rstrip()
ans = i = 0
while i <= len(S) - len(s):
    if S[i:i+len(s)] == s:
        ans += 1
        i += len(s)
    else:
        i += 1
print(ans)