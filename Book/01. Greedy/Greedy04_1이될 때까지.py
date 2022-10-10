def solution(n, k):
    cnt = 0
    while True:
        target = (n//k) * k # n을 k로 나눈 몫에 k를 곱해줌(17//4 -> 4 * 4 = 16도출)
        cnt += (n-target) # 17-16 = 1 더해줌
        n = target

        if n<k: # 반복문 탈출 조건
            break

        # k로 나누기
        cnt += 1
        n //= k

    cnt += (n-1) # 위 식으로 인해 1이 더해졌으므로 마지막에 빼주기
    return cnt

solution(17, 4) # 확인용
