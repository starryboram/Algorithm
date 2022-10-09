def solutions(nums):
    answer = 0
    num = int(len(nums)/2)
    arr = list(set(nums))

    if len(arr) > num:
        answer = num
    else:
        answer = len(arr)
    return answer

"""### 충격"""

def solution(ls):
    return min(len(ls)/2, len(set(ls)))
