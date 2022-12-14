def solution(brown, yellow):
    arr = [i for i in range(2, brown + yellow-1) if (brown + yellow)%i == 0]
    if len(arr) == 1:
        return [arr[0], arr[0]]
    else:
        while True:
            if (arr[0]-2) * (arr[-1]-2) == yellow:
                return [arr[-1], arr[0]]
            else:
                arr.pop(0)
                arr.pop(-1)

# 다른 풀이(진정한 수학과)
def solution(brown, yellow):
    for i in range(1, int(yellow**(1/2))+1): # 반만 계산
        if yellow % i == 0: # 약수이고
            if 2*(i + yellow//i) == brown-4: # 가로*2 + 세로*2 - 겹치는부분 4
                return [yellow//i+2, i+2]