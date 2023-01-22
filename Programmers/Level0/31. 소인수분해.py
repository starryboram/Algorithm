# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/120852
def solution(n):
    answer = [i for i in range(2,n+1) if n%i == 0]
    arr = []
    result = []
    for i in answer:
        for j in range(1,i+1):
            if i%j == 0:
                arr.append(j)
        if len(arr) > 2:
            arr = []
        else:
            result.append(i)
            arr = []
    return result

# 다른 사람 풀이
def solution(n):
    k = 2
    answer = []
    while n>1:
        if n%k==0:
            answer.append(k)
            while n%k==0:
                n//=k
        k+=1

    return answer


# 함수 2번 쓰기
def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if not n%i:
            return False
    return True

def solution(n):
    answer = []
    for i in range(2,n+1):
        if not n%i and is_prime(i):
            answer.append(i)
    return answer