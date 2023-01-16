# num_list = [1, 2, 3, 4, 5, 6, 7, 8] / n = 2 / result = [[1, 2], [3, 4], [5, 6], [7, 8]]
# num_list = [100, 95, 2, 4, 5, 6, 18, 33, 948] / n = 3 / result = [[100, 95, 2], [4, 5, 6], [18, 33, 948]]

def solution(num_list, n):
    answer = []
    arr = []
    for i in num_list:
        arr.append(i)
        if len(arr) == n:
            answer.append(arr)
            arr = []
    return answer

# 다른 사람 풀이
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer


## 잘라서 배열로 저장하기(똑같은 문제)
def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]