# 체스판 다시 칠하기
a, b = map(int, input().split())
lst = []
for i in range(a):
    lst.append(input())

ans =[]
for i in range(b - 7):
    for j in range(a - 7):
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        for k in range(j, j + 8):
            for l in range(i, i+8, 2):
                if lst[k][l] == lst[k][l+1]:
                    cnt1 += 1
                else:
                    if k % 2 == 0:
                        if lst[k][l] == 'W':
                            cnt2 += 2
                        else:
                            cnt3 += 2
                    else:
                        if lst[k][l] == 'B':
                            cnt2 += 2
                        else:
                            cnt3 += 2
        if cnt1 + cnt3 > cnt1 + cnt2:
            ans.append(cnt1 + cnt2)
        else:
            ans.append(cnt1 + cnt3)

print(min(ans))