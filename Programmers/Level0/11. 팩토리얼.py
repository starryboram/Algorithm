def solution(n):
    arr = [1]
    for i in range(2,11):
        arr.append(i*arr[-1])
    
    if n == 1:
        return 1
    else: 
        for i in range(1, len(arr)):
            if n == arr[i]:
                return i + 1
            elif n < arr[i] and n > arr[i-1]:
                return i

# 팩토리얼 함수가 따로 있다!!!!!!!!!
from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k