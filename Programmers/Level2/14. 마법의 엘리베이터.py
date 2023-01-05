def solution(storey):
    answer = 0
    while storey:
        rest = storey % 10 # 나머지 = 1의 자리 수
        if rest > 5: # 5~9사이의 rest 갖는 경우 
            answer += (10 - rest) # 위로 올라가는게 더 빠름
            storey += 10 # 10의 자리를 하나 더해주고
        elif rest < 5: # 1~4의 나머지를 갖는 경우
            answer += rest # 아래로 내려가는게 더 빠름
        else: # 1의 자리 수가 5일경우
            if (storey // 10) % 10 > 4: # 10의자리 수가 5 이상인 경우에는
                storey += 10 # 10의자리 1개 더해줌
            answer += rest # 10의자리 수가 0~4 사이인 경우 나머지값 더해줌
        storey //= 10 

    return answer
                
# 위의 코드는 떠오르지 않아서 블로그를 참고했다. 일주일 후에 다시 풀어봐야지
# 5일 때 어떻게 할지 정하는 것이 핵심!