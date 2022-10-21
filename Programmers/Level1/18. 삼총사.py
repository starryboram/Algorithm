# 삼총사 - 내풀이(다른 사람들이 푼 풀이랑 비슷)
import itertools
def solution(number):
    result = list(itertools.combinations(number,3))
    answer = 0
    for i in range(len(result)):
        if sum(result[i]) == 0:
            answer += 1
    return answer