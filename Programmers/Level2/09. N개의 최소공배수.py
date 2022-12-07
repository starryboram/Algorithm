from functools import reduce
def solution(arr):
    a = reduce(lambda i,j : i*j, arr)
    cnt = 0
    for i in range(max(arr), a+1):
        for j in arr:
            if i%j == 0:
                cnt += 1
        if cnt == len(arr):
            return i
        else:
            cnt = 0


# 다른 사람 풀이 - 처음보는 함수다.
from fractions import gcd
def nlcm(num):      
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer