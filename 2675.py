for _ in range(int(input())):
    n, s = input().split()
    ans = ''
    for i in s:
        ans += i * int(n)
    print(ans)