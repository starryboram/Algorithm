def solution(A,B):
    answer = 0
    for i,j in zip(sorted(A), list(reversed(sorted(B)))):
        answer += i*j
    return answer

# 람다식으로 표현한 풀이법
def getMinSum(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
    