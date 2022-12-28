def solution(food):
    answer = ""
    for i in range(1, len(food)):
        if food[i]%2 == 0:
            answer += str(i)*(food[i]//2)
        else:
            answer += str(i)*((food[i]-1)//2)
    answer += "0"
    answer += answer[-2::-1]
    return answer

# 다른 풀이
def solution(food):
    answer = ''
    for i,n in enumerate(food[1:]):
        answer += str(i+1) * (n//2)
    return answer + "0" + answer[::-1]