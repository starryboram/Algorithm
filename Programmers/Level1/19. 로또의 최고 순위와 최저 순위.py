# 로또의 최고 순위와 최저 순위 - 내풀이
def solution(lottos, win_nums):
    if sorted(lottos) == sorted(win_nums):
        return [1,1]
    else:  
        if lottos == [0,0,0,0,0,0]:
            return [1,6]
        else:
            cnt = 0
            for i in lottos:
                for j in win_nums:
                    if i == j:
                        cnt += 1
            zero = 0
            for i in lottos:
                if i == 0:
                    zero += 1
            
            if cnt == 0 and zero == 0:
                return [6,6]
            else:
                return [7-(cnt+zero), 7 - cnt]

# 다른 사람 풀이
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

# 다른 사람 풀이2 - 현타....오는 중.....
def solution(lottos, win_nums):
    rank = { 0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]