# 문제 해석대로 풀이 
def solution(n):
    cnt = 0
    while True:
        if n%2 == 0:
            if n == 1:
                break
            else: 
                n = int(n/2)
                cnt += 1
        else:
            if n == 1:
                break
            else:
                n = n*3 + 1
                cnt += 1
    if cnt > 500:
        return -1
    else:
        return cnt


# 간편한 코드
def solution(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1