def solution(k, m, score):
    score = reversed(sorted(score))
    result = 0
    arr = []
    for i in score:
        arr.append(i)
        if len(arr) == m:
            result += min(arr) * m
            arr = []
    return result


# 다른 사람 풀이
def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m