# array 배열로 주어질 때, 키 큰 사람의 숫자를 세어서 나타내주기
def solution(array, height):
    answer = 0 
    for i in array:
        if i > height:
            answer += 1
    return answer

# 간추리기
def solution(array, height):
    return sum(1 for a in array if a > height)