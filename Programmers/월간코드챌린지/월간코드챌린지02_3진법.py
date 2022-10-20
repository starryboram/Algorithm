# 초기 - 내풀이
def solution(n):
    array_3 = []
    answer = 0
    while True:
        array_3.append(n%3)
        n = n//3
        if n < 3:
            array_3.append(n)
            break

    for i in range(len(array_3)):
        answer += array_3[i]*(3**(len(array_3) - i-1))
    return answer

# 테스트 1 통과 못함 -> 이유 분석 -> n이 3보다 작은 수에 대해서 올바르게 출력이 안됨
# 코드 수정(n이 3보다 클 때, 아닐 때로 만듦)

# 완료 - 내풀이(통과)
def solution(n):
    array_3 = []
    answer = 0
    if n >= 3:
        while True:
            array_3.append(n%3)
            n = n//3
            if n < 3:
                array_3.append(n)
                break

        for i in range(len(array_3)):
            answer += array_3[i]*(3**(len(array_3) - i-1))
        return answer
    else:
        return n


# 다른 사람 풀이
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer