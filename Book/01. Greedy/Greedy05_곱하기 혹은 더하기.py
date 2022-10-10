# 내 풀이
def solution(s):
    answer = int(s[0])
    for i in range(1, len(s)):
        if int(s[i]) <= 1 or answer <= 1:  # 0이나 1이 있을 경우에는 무조건 더해야함
            answer += int(s[i])
        else:
            answer *= int(s[i]) 
    return answer
solution('01011')