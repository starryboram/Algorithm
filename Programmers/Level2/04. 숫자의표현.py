def solution(n):
    answer = 1
    for i in range(1,n):
        sum_i = 0
        for j in range(i, n):
            sum_i += j
            if sum_i == n:
                answer += 1
                break
            if sum_i > n:
                break
    return answer