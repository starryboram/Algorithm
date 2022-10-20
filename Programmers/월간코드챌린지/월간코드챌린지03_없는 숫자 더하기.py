# 없는 숫자 더하기 - 내 풀이
def solution(numbers):
    return sum([1,2,3,4,5,6,7,8,9,0]) - sum(numbers)

# 다른 사람 풀이(정석)
def solution(numbers):
    return sum([i for i in [1,2,3,4,5,6,7,8,9,0] if i not in numbers])

# set 이용한 풀이
def solution(numbers):
    return sum(set(range(10)) - set(numbers))