# number1:1, denom1:2, numer2:3, denom2: 4일떄 1 / 2 + 3 / 4 = 5 / 4입니다. 따라서 [5, 4]를 return 합니다.
# number1:9, denom1:2, numer2:1, denom2: 3일떄 9 / 2 + 1 / 3 = 29 / 6입니다. 따라서 [29, 6]을 return 합니다.
import math
def solution(numer1, denom1, numer2, denom2):
    a = (numer1*denom2)+(numer2*denom1)
    b = denom1*denom2
    c = math.gcd(a,b)
    return [a//c, b//c]

# 다른 사람의 풀이(faction이용)
# import fractions #공약수가 존재하는 경우, 자동으로 제거
# fractions.Fraction(4,16) => Fraction(1, 4)
# fractions.Fraction(-6,21) => Fraction(-2, 7)

from fractions import Fraction
def solution(denum1, num1, denum2, num2):
    answer = Fraction(denum1, num1) + Fraction(denum2, num2)
    return [answer.numerator, answer.denominator]

# 다른 사람 풀이(모듈안씀)
def solution(denum1, num1, denum2, num2):
    answer = []
    s = 0

    denum0 = (denum1*num2) +(denum2*num1)
    num0 = num1*num2

    for i in range(min(denum0,num0),0,-1):
        if denum0%i == 0 and num0%i == 0:
            s = i
            break

    denum0 /= s
    num0 /= s
    answer.append(denum0)
    answer.append(num0)

    return answer