# 문자 바꾸기
# 문자열.replace(바꾸고 싶은 문자열, 문자열 어떻게 바꿀지)

# 공백 제거하기
# 문자열.strip()

def solution(babbling):
    cnt = 0
    for i in babbling: 
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i: # 중복되지 않을 경우
                i=i.replace(j,' ') # 해당 문자열 공백으로 만들고
        if len(i.strip())==0: # 공백일경우 cnt += 1
            cnt +=1
    return cnt

    # 다시 풀어보기!