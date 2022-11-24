def solution(s):
    answer = []
    cnt0 = 0
    cnt = 0
    while True:      
        for i in s:
            if i == '1':
                answer.append(i)
            elif i == '0':
                cnt0 += 1
        if len(answer) == 1:
            cnt += 1
            return [cnt, cnt0]
        else:
            s = bin(len(answer))[2:]
            answer = []
            cnt += 1


# 다른 사람 풀이(아...놔....)
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]