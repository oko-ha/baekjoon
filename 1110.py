# https://www.acmicpc.net/problem/1110
# 이름 : 더하기 사이클
# 번호 : 1110
# 난이도 : 브론즈 I
# 분류 : 수학, 구현, 문자열

n = int(input())
if n < 10:
    n *= 10
index = 0
temp = str(n)
while True:
    index += 1
    if int(temp) == 0:
        break
    t1 = temp[1]
    t2 = str(int(temp[0]) + int(temp[1]))
    if len(t2) == 2:
        temp = t1 + t2[1]
    else:
        temp = t1 + t2
    if int(temp) == n:
        break
print(index)