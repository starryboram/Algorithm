# 문제:https://school.programmers.co.kr/learn/courses/30/lessons/120923
# 얘는 다시 한번 풀어봐야겠다.
def solution(num, total):
    average = total // num
    return [i for i in range(average - (num-1)//2, average + (num + 2)//2)]