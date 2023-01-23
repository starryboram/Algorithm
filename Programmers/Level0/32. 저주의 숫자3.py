# https://school.programmers.co.kr/learn/courses/30/lessons/120871
# 얘는 규칙을 몰라서 코드를 참고했다. 
def solution(n):
    answer = 0
    for i in range(n):
        answer += 1
        while answer%3 == 0 or '3' in str(answer):
            answer += 1
    return answer