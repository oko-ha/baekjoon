def solution(n):
    dic = {}
    for i in n:
        for j in range(2):
            if i[j] in dic:
                dic[i[j]] += 1
            else:
                dic[i[j]] = 1
    answer = []
    for a, b in dic.items():
        if b == 1:
            answer.append(a)
    return answer

n = [[3, 10], [3, 4], [4, 10]]
print(solution(n))