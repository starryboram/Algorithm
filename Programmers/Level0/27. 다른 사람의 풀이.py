# 등비수열 혹은 등차수열로 이루어진 배열이 주어졌을 때, 그 후에 올 숫자 리턴하기
# common = [1, 2, 3, 4] / return 5
# common = [2, 4, 8] / return 16
def solution(common):
    for i in range(1, len(common)):
        if 2*common[i] == common[i-1] + common[i+1]:
            return common[-1] + common[2]-common[1]
        else:
            return common[-1] * (common[1]//common[0])

# 다른사람 풀이(왜이리 간편해 보이지 발상은 똑같음)
def solution(common):
    answer = 0
    a,b,c = common[:3]
    if (b-a) == (c-b):
        return common[-1]+(b-a)
    else:
        return common[-1] * (b//a)
    return answer