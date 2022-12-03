def solution(s):
    arr = list(map(int, s.split(' ')))
    return "{} {}".format(sorted(arr)[0], sorted(arr)[-1])

