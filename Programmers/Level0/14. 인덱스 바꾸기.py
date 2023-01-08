def solution(my_string, num1, num2):
    a,b = my_string[num1], my_string[num2]
    answer = ""
    for i in range(len(my_string)):
        if i == num1:
            answer += str(b)
        elif i == num2:
            answer += str(a)
        else:
            answer += str(my_string[i])
    return answer

# ㅎ......
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s)