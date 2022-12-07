def solution(n):
    array = [0, 1]
    if n == 2:
        return 2
    else:
        while True:
            array.append(array[-1] + array[-2])
            if len(array) == n:
                return (array[-1] + array[-2]) % 1234567
                break

# 다른 사람 풀이 ....? 실화인가
def fibonacci(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    return a
