def solution(n):
    if n == 1:
        return 1
    else:
        cnt = 0
        while True:
            if n<= 0:
                return cnt
            else:
                if n%2 == 1:
                    cnt += 1
                    n = n//2
                else:
                    n = n//2

# 다른 사람 풀이 ........?ㅎ.......
def solution(n):
    return bin(n).count('1')