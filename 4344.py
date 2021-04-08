# 평균은 넘겠지
n = int(input())
ans = []
for i in range(n):
    lst = list(map(int, input().split()))
    lg = lst.pop(0)
    avg = sum(lst)/lg
    cnt = 0
    for i in lst:
        if i > avg:
            cnt += 1
    ans.append((round(cnt/lg * 100, 3)))

for i in ans:
    print('%.3f%%' % i)