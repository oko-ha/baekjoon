# https://www.acmicpc.net/problem/1038
# 이름 : 감소하는 수
# 번호 : 1038
# 난이도 : 골드 V
# 분류 : 브루트포스 알고리즘, 백트래킹

import sys
n = int(sys.stdin.readline().rstrip())
if n < 10:
    print(n)
elif n > 1022:
    print(-1)
else:
    arr = [i for i in range(1, 10)]
    num = [10]
    # 자리수 구하기
    while arr:
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
        num.append(num[-1] + arr.pop())
    for i in range(1, len(num)):
        if n < num[i]:
            digit = i + 1
            n -= num[i - 1]
            break
    arr = [-1] * digit
    # 감소하는 수인지?
    def isDec(k):
        if k == 0 or arr[k - 1] > arr[k]:
            return True
        return False
    # 감소하는 수 backtracking
    def decN(k):
        global cnt

        if k < digit:
            for i in range(10):
                arr[k] = i
                if isDec(k):
                    decN(k + 1)
                    if cnt == n:
                        return arr
        else:
            cnt += 1
    cnt = -1
    decN(0)
    print(''.join(map(str, arr)))