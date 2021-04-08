# A+B -5
ans = []
while True:
    ans.append(sum(map(int, input().split())))
    if ans[-1] == 0: break
for i in ans[:-1]:
    print(i)