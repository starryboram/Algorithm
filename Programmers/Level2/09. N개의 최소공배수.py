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
# gcd란? a와 b의 최대공약수는 'b'와 'a를 b로 나눈 나머지'의 최대공약수와 같다. 즉, gcd(a,b) = gcd(b, a % b)이다. 
# 어떤 수와 0의 최대공약수는 자기 자신이다. 즉, gcd(n, 0) = n이다.
from fractions import gcd
def nlcm(num):      
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer

# 과연 내가 이 알고리즘을 안 까먹고 사용할 수 있을 것인가....