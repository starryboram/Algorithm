def solution(a, b):
    m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    dday = sum(m[:a-1]) + b
    return d[dday%7]
