def solution(n):
    answer = 0
    coin = [500, 100, 50, 10]
    
    for i in coin:
        answer +=  n//i # 1260원을 coin으로 나눈 몫만큼 더해줌
        n %= i # 나머지 260원을 n으로 만듦 (위 과정 반복)

    return answer

n = 1260
solution(n) # 확인용