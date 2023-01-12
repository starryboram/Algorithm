# [1,1,3,3,3,4] => 최빈값 3 도출
# [1,1,3,3] => 최빈값이 두 개 이상이니까 -1 리턴
from collections import Counter
def solution(array):
    if len(set(array)) == 1:
        return array[0]
    else:
        if Counter(array).most_common()[0][1] == Counter(array).most_common()[1][1]:
            return -1
        else:
            return Counter(array).most_common()[0][0]

# 다른사람 풀이
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1