# 6조각 내주는 피자 집에서 피자를 주문할 때, n명이 주문한 피자를 동등하게 남기지 않고 먹기 위한 피자수 리턴
# 4명이서 피자 먹기 위해서는 피자를 2판 시켜야 함(12조각이니까)
# 10명이서 피자 먹기 위해서는 피자를 5판 시켜야 함(30조각이니까)
# 즉, 최소공배수 구하는 문제!

def solution(n):
    for i in range(min(n, 6), n*6+1):
        if i%6 == 0 and i%n == 0:
            return int(i//6)

# 다른 풀이
import math
def solution(n):
    return (n * 6) // math.gcd(n, 6) // 6 


# math함수에 대해서 알아보기
# 최대공약수 구할 때: gcd 함수 쓰기
import math
math.gcd(3,6) # 3반환
math.gcd(4,8) # 4반환 
math.gcd(66, 22, 11) # 11 반환

# 최소공배수 구할 때: lcm 함수 쓰기
math.lcm(2) # 2 반환
math.lcm(2, 4) # 4 반환
math.lcm(66, 22, 11) # 66 반환
# 인자가 없는 경우(인자가 0개) 경우에, 즉 math.lcm() 은 함수의 반환 값은 1
# 인자 중에 하나라도 0인 경우에는 당연하게도 0이 반환
 