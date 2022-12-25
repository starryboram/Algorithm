def solution(X, Y): # 1차 시도 : 73.7점(시간초과 뜸)
    answer = []
    X = sorted(list(X))
    Y = sorted(list(Y))
    for i in X:
        if i in Y:
            answer.append(i)
            Y.remove(i)
    
    if len(answer) == 0:
        return "-1"
    else:
        arr = list(reversed(sorted(answer)))
        if arr[0] == "0":
            return "0"
        else:
            return ''.join(arr)

# 다른 방법으로 풀이함(min값에 따라 계산하게끔) => 100점(통과)
def solution(X, Y):
    arr_X = []
    arr_Y = []
    for i in range(10):
        arr_X.append(X.count(str(i)))
        arr_Y.append(Y.count(str(i)))
    
    answer = []
    for i,j in zip(arr_X, arr_Y):
        answer.append(min(i,j))
    
    result = ""    
    for i in range(len(answer)):
        if answer[i] >= 1:
            result += str(i) * answer[i]
    
    result = result[::-1]
    if result == "":
        return "-1"
    else:
        if result[0] == "0":
            return "0"
        else:
            return result

#다른 사람 풀이
def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer