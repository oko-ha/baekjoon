# https://www.acmicpc.net/problem/2108
# 이름 : 통계학
# 번호 : 2108
# 난이도 : 실버 IV
# 분류 : 구현, 정렬

import sys
arr = []
dic = {}
sum = 0
i = int(sys.stdin.readline().rstrip())
for _ in range(i):
    n = int(sys.stdin.readline().rstrip())
    sum += n
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1
    arr.append(n)
arr.sort()
dic = sorted(dic.items(), key=lambda x : (-x[1], x[0]))
print(round(sum/i))
print(arr[i//2])
if len(dic) > 1 and dic[0][1] == dic[1][1]:
    print(dic[1][0])
else:
    print(dic[0][0])
print(arr[-1] - arr[0])