def solution(arr):
    newarr = []
    for i in range(len(arr)):
        if i == 0:
            newarr.append(arr[i])
        elif arr[i] != arr[i-1]:
            newarr.append(arr[i])
    return newarr