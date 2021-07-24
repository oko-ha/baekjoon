# https://www.acmicpc.net/problem/2596
# 이름 : 비밀편지
# 번호 : 2596
# 난이도 : 브론즈 II
# 분류 : 구현, 문자열

import sys
input = sys.stdin.readline
N = int(input())
S = input().strip()
arr = ['000000', '001111', '010011', '011100', '100110', '101001', '110101', '111010']
ans = ''
for i in range(0, len(S), 6):
    temp = []
    for j in range(8):
        cnt = 0
        for a, b in zip(arr[j], S[i:i+6]):
            if a != b:
                cnt += 1
            if cnt > 1:
                break
        if cnt < 2:
            temp.append(chr(65 + j))
    if len(temp) != 1:
        print(len(ans) + 1)
        exit(0)
    else:
        ans += temp[0]
print(ans)