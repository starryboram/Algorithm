def solution(s): 
    arr = []
    for i in s:
        if len(arr) == 0: # arr이 비어있을 경우 s의 문자 추가 
            arr.append(i)
        elif arr[-1] == i: # arr의 마지막 문자열 값이 s와 같을 경우 arr에 있는 마지막 값 pop
            arr.pop()
        else: # arr에 들어 있는 값과 i가 같지 않을 경우 arr에 추가
            arr.append(i)
            
    if len(arr) == 0: 
        return 1
    else: 
        return 0 