def solution(n, words):
    cnt = 1
    count = 1
    answer = [words[0]]
    for i in words[1:]:
        if i in answer: # 틀림
            cnt += 1
            if cnt > n :
                cnt = 1
                count += 1
            return [cnt, count]
        else: # 계속 진행 가능
            if answer[-1][-1] == i[0]:
                answer.append(i)
                cnt += 1
                if cnt > n:
                    cnt = 1
                    count += 1
            else: # 끝말잇기 못했을 경우
                cnt += 1
                if cnt > n:
                    cnt = 1
                    count += 1
                return [cnt, count]
    
    return [0,0]

    # 다른 풀이
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]