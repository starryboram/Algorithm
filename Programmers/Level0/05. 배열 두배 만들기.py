# 배열의 원소를 각각 2배씩 곱하기
# [1,2,3,4,5] -> [2,4,6,8,10]
def solution(numbers):
    return [2*i for i in numbers]

# 다른 풀이
def solution(numbers):
    return list(map(lambda x: x * 2, numbers))

