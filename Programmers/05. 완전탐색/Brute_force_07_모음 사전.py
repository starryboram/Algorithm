import itertools
def solution(word):
    w = ['A','E','I','O','U']*5
    a = []
    for i in range(1, 6):
        a.append(list(map(''.join, itertools.combinations(w,i))))
        a2 = list(itertools.chain(*a))
    return sorted(set(a2)).index(word) +1