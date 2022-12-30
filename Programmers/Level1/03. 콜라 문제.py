def solution(a, b, n):
    cnt, coke = 0, 0
    while True:
        coke += int(n//a)*b
        n = n - (int(n//a) * a) + (int(n//a)*b)
        
        if n < a:
            return coke


# 다른 사람 풀이 읭?
solution = lambda a, b, n: max(n - b, 0) // (a - b) * b

# 다른 사람 풀이2
def solution(a, b, n):
    answer = 0

    num = n
    while num >= a:
        cnt = num // a
        num -= (cnt * a)
        num += (cnt * b)
        answer += (cnt * b)


    return answer