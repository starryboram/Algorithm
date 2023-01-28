def solution(dots):
    dots = sorted(dots)
    if abs(dots[1][1]-dots[0][1]) / abs(dots[1][0]-dots[0][0]) == abs(dots[3][1]-dots[2][1]) / abs(dots[3][0]-dots[2][0]):
        return 1

    else:
        return 0

# 다른 사람 풀이
from itertools import combinations

def solution(dots):
    a = []
    for (x1,y1),(x2,y2) in combinations(dots,2):
        a.append((y2-y1,x2-x1))

    for (x1,y1),(x2,y2) in combinations(a,2):
        if x1*y2==x2*y1:
            return 1
    return 0