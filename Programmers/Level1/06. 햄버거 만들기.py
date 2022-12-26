def solution(ingredient):
    answer = []
    result = 0
    for i in ingredient:
        if len(answer) <= 2:
            answer.append(i)
        else:
            if i == answer[-3] and ((answer[-3] + 1) == answer[-2]) and ((answer[-2] + 1) == answer[-1]):
                result += 1
                answer.pop(-1)
                answer.pop(-1)
                answer.pop(-1)
            else:
                answer.append(i)
    return result


# 다른 사람 풀이
def solution(ingredient):
    s = []
    answer = 0
    for i in ingredient:
        s.append(i)
        while s[-4:] == [1, 2, 3, 1]:
            s.pop()
            s.pop()
            s.pop()
            s.pop()
            answer += 1

    return answer


# 다른 사람 풀이2
def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for i in range(4):
                s.pop()
    return cn