# 평균
input()
lst = list(map(int, input().split()))
m = max(lst)
sum = 0
for i in lst:
    sum += i / m * 100
print(sum/len(lst))