# 어떤 n이 주어졌을 때 제곱수가 있으면 1 아니면 2 반환하기
# n = 144이면 제곱수 12가 있으니까 1 반환
# n = 77이면 제곱수 없으므로 0반환

def solution(n):
    for i in range(1001):
        if i*i  == n:
            return 1
        else:
            pass
    return 2 # 나는 항상 단순of단순이다. 머리 단순~

# 다른 사람 풀이1
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2

# 다른 사람 풀이2
def solution(n):
    return 1 if (n ** 0.5) % 1 == 0 else 2