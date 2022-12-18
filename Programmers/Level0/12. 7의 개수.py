# array = [7, 77, 17]일 때 7의 갯수를 세서 4를 return 해주세요.
def solution(array):
    return sum(1 for i in array for j in range(len(str(i))) if str(i)[j] == '7')

# 다른 사람 풀이(어렵게 생각하지 말기)
def solution(array):
    return str(array).count('7')

# 또 다른 풀이
def solution(array):
    return ''.join(map(str, array)).count('7')