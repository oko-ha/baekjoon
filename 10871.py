# X보다 작은 수
a, b = map(int, input().split())
lst = list(map(int, input().split()))
for i in lst:
    if i < b:
        print(i, end=" ")