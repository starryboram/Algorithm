def solution(operations):
    arr = []
    for i in operations:
        if i == "D 1": #최댓값
            if len(arr) >= 1:
                arr = sorted(arr)
                arr.pop()
            else:
                pass
        elif i == "D -1": #최솟값
            if len(arr) >= 1:
                arr = sorted(arr)
                arr.pop(0)
            else:
                pass
        else:
            arr.append(int(i[2:]))
            
    if len(arr) == 0:
        return [0,0]
    else:
        return [max(arr), min(arr)]

# 다른 풀이(힙을이용한 풀이 : 얘는 공부 더 하고 올릴예정)