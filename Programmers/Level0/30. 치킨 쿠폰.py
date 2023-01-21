# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/120884
def solution(chicken):
    answer = 0
    while True:
        if chicken >= 10:
            answer += chicken//10
            chicken = chicken//10 + chicken%10
        else:
            return answer

# 다른 사람 풀이
def solution(chicken):
    return int(chicken*0.11111111111)

# 다른 사람 풀이2
def solution(chicken):
    answer = (max(chicken,1)-1)//9
    return answer