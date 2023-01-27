def solution(polynomial):
    polynomial = polynomial.replace(" ","")
    arr = polynomial.split('+')
    x_answer = 0
    cnt = 0
    for i in arr:
        if 'x' in i:
            if len(i) == 1:
                x_answer += 1
            else:
                x_answer += int(i[:-1])
        else:
            cnt += int(i)
    
    if x_answer == 0 and cnt != 0:
        return str(cnt)
    elif x_answer == 0 and cnt == 0:
        return "0"
    elif x_answer == 1 and cnt >= 1:
        return "x" + " + " + str(cnt)
    elif x_answer == 1 and cnt == 0:
        return "x"
    elif x_answer != 0 and cnt >= 1 :
        return str(x_answer) + "x" + " + " + str(cnt)
    else:
        return str(x_answer) + "x"

