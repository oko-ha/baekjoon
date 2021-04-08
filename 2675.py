# https://www.acmicpc.net/problem/2675
# 이름 : 문자열 반복
# 번호 : 2675
# 난이도 : 브론즈 II
# 분류 : 구현

for _ in range(int(input())):
    n, s = input().split()
    ans = ''
    for i in s:
        ans += i * int(n)
    print(ans)