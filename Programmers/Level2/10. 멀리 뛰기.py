def solution(n): # 피보나치수... 로 풀어도 풀림
    a = [1, 2]
    if n == 1: 
        return 1
    elif n == 2:
        return 2
    else:
        while True:
            if n == len((a)):
                return a[-1]%1234567
            else:
                a.append(a[-1] + a[-2])

# 다른 사람 풀이
def jumpCase(num):
    a, b = 1, 2
    for i in range(2,num):
        a, b = b, a+b
    return b