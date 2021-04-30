# https://www.acmicpc.net/problem/12015
# 이름 : 가장 긴 증가하는 부분 수열 2
# 번호 : 12015
# 난이도 : 골드 II
# 분류 : 이분 탐색, 가장 긴 증가하는 부분 수열: O(n log n)

# binary search 구현
import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
lis = [arr[0]]
for i in range(1, n):
    if lis[-1] < arr[i]:
        lis.append(arr[i])
    else:
        left, right = 0, len(lis)
        while left <= right:
            mid = (left + right) // 2
            if lis[mid] > arr[i]:
                index = mid
                right = mid - 1
            elif lis[mid] < arr[i]:
                left = mid + 1
            else:
                index = mid
                break
        lis[index] = arr[i]
print(len(lis))

# bisect 모듈 사용
from bisect import bisect_left
lis.clear()
lis = [arr[0]]
for i in range(1, n):
    if lis[-1] < arr[i]:
        lis.append(arr[i])
    else:
        lis[bisect_left(lis, arr[i])] = arr[i]
print(len(lis))