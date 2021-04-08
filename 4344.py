# https://www.acmicpc.net/problem/4344
# 이름 : 평균은 넘겠지
# 번호 : 4344
# 난이도 : 브론즈 I
# 분류 : 수학, 사칙연산

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