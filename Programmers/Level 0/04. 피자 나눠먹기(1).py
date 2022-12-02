# 7조각으로 자르는 피자. n은 사람 수. 몇판 시켜야 할까?(못먹는 사람 없게끔)
import math
def solution(n):
    return math.ceil(n/7)

# 신박한 풀이
def solution(n):
    return (n - 1) // 7 + 1