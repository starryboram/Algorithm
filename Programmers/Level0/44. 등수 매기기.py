# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/120882
def solution(score):
    arr = [sum(i)/len(i) for i in score]
    arr_sort = sorted(arr, reverse = True)
    return [arr_sort.index(i) + 1 for i in arr]
    # 추후 다시 풀어보기