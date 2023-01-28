def solution(dots):
    if dots[0][0] == dots[1][0]:
        return abs((dots[0][1] - dots[1][1]) * (dots[0][0] - dots[2][0]))
    elif dots[0][0] == dots[2][0]:
        return abs((dots[0][1] - dots[2][1]) * (dots[0][0] - dots[1][0]))
    else:
        return abs((dots[0][1] - dots[3][1]) * (dots[0][0] - dots[1][0]))

# 다른 사람 풀이
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])
