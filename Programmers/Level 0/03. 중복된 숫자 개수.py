# 배열 안에서 중복된 숫자 합 구하기
def solution(array, n):
    return sum(1 for i in array if i == n)

# 다른 풀이
def solution(array, n):
    return array.count(n)