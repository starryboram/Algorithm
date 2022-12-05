# strlist의 원소의 길이를 결과값으로 출력하기
# ["I", "Love", "Programmers."] -> [1, 4, 12]
def solution(strlist):
    return [len(i) for i in strlist]

# 다른 풀이
def solution(strlist):
    return list(map(lambda v: len(v), strlist))