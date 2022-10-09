ef solution(numbers, target):
    answer = 0
    arr = [0]
    for num in numbers:
        tmp = []
        for a in arr:
            tmp.append(a + num)
            tmp.append(a - num)
        arr = tmp
    
    for i in arr:
        if i == target:
            answer += 1
    return answer
