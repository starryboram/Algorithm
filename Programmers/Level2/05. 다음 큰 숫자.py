def solution(n):
    s = bin(n)[2:]
    num = s.count('1')
    if len(s) == num:
        return int('0b10'+('1'*(len(s)-1)),2)
    else:
        for i in range(n+1,1000000):
            big = bin(i)[2:]
            num2 = big.count('1')
            if num == num2:
                return i
# 생각해보니까 for i in range(n+1, 1000000, 2)로 해도 괜찮을 것 같다.
# 1이 더해졌다는건 1의 갯수가 더 많다는 것이기 때문에,
# 반만 계산하게 되어 효율성 측면에서 더 좋아진다.

# 개편 전 - 지금은 효율성에 걸림
def nextBigNumber(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n

