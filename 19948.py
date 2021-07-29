# https://www.acmicpc.net/problem/19948
# 이름 : 음유시인 영재
# 번호 : 19948
# 난이도 : 실버 III
# 분류 : 구현, 문자열, 파싱

import sys
input = sys.stdin.readline
def numbering():
    S = list(input().split())
    n = int(input())
    arr = list(map(int, input().split()))
    ans = ''
    if len(S) - 2 > n:
        return -1
    for s in S:
        temp = 0
        for i in range(len(s)):
            if i == 0:
                ans += s[i].upper()
            asc = ord(s[i])
            if asc == temp:
                continue
            if 64 < asc < 91:
                if arr[asc - 65] > 0:
                    arr[asc - 65] -= 1
                else:
                    return -1
            else:
                if arr[asc - 97] > 0:
                    arr[asc - 97] -= 1
                else:
                    return -1
            temp = asc
    temp = 0
    for a in ans:
        asc = ord(a)
        if asc == temp:
            continue
        if 64 < asc < 91:
            if arr[asc - 65] > 0:
                arr[asc - 65] -= 1
            else:
                return -1
        else:
            if arr[asc - 97] > 0:
                arr[asc - 97] -= 1
            else:
                return -1
        temp = asc
    return ans
print(numbering())