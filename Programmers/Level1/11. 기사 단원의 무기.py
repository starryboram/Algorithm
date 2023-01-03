# 처음 풀이 # 27개 중 9개 시간초과 : 66.7점
def solution(number, limit, power):
    if number == 1:
        return 1
    else:
        arr = [1]
        cnt = 1
        for i in range(2, number+1):
            for j in range(1, i):
                if i%j == 0:
                    cnt += 1
            arr.append(cnt)
            cnt = 1
        
        sum = 0
        for i in arr:
            if i <= limit:
                sum += i
            else:
                sum += power
        return sum

# 두번째 풀이
# 소수 개수 구하기
def sosu(n):
    sosu = []
    for i in range(1, int(n**0.5) + 1):
        if n%i == 0:
            sosu.append(n//i)
            sosu.append(i)
    return len(set(sosu)) # 25가 주어졌을 경우 5가 두번 들어가기때문에 중복 제거 해줘야 함

# 철의 무게 구하기
def solution(number, limit, power):
    sum = 0
    for n in range(number+1):
        if sosu(n) > limit:
            sum += power
        else:
            sum += sosu(n)
    return sum