# 문제 풀이: https://school.programmers.co.kr/learn/courses/30/lessons/120956
from itertools import permutations
def solution(babbling):
    speek = ["aya","ye","woo","ma"]
    word = [''.join(j) for i in range(1, len(speek)+1) for j in permutations(speek, i) ]

    return sum([1 for i in babbling if i in word])