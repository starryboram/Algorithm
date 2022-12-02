# 정수 배열의 평균값을 나타내기기
def solution(numbers):
    return sum(numbers)/len(numbers)


# 다른 풀이
import numpy as np
def solution(numbers):
    return np.mean(numbers)