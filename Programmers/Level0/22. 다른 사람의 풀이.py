# balls중 share의 조합으로 나타낼 수 있는 수 리턴
# 3개의 다른 balls 존재. 2개 뽑아서 나타낼 수 있는 경우의 수 말해주기
# (1,2), (1,3), (2,3) => 3 리턴

#  4개 시간초과 뜸
from itertools import combinations
def solution(balls, share):
    return len(list(combinations(range(0, balls), min(share, balls-share))))

# 팩토리얼 이용해서 풀기
import math
def solution(balls, share):
    return math.factorial(balls) / (math.factorial(balls-share) * math.factorial(share))

# 다른 풀이
import math
def solution(balls, share):
    return math.comb(balls, share)