# https://www.acmicpc.net/problem/1316
# 이름 : 그룹 단어 체커
# 번호 : 1316
# 난이도 : 실버 V
# 분류 : 구현, 문자열

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