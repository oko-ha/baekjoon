ans = 0
for _ in range(int(input())):
    s = input()
    h = {}
    temp =''
    for i in s:
        if temp != i:
            if i in h:
                ans -= 1
                break
            else:
                h[i] = 1
        temp = i
    ans += 1
print(ans)