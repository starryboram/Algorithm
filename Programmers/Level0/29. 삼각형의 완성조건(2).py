# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/120868
def solution(sides):
    sides = sorted(sides)
    arr = len([i for i in range(sides[-1]-sides[0]+1, sides[-1]+1)])
    brr = len([i for i in range(sides[-1]+1, sum(sides))])
    return arr + brr

# 다른 풀이ㅋ...
def solution(sides):
    return sum(sides) - max(sides) + min(sides) - 1