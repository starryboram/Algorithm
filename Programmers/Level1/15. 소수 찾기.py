def solution(n):
    numbers = [True] * (n + 1)
    cnt = 0

    for i in range(2,int(n**0.5)+1):
        if numbers[i] == False:
            continue;

        for j in range(2*i,n+1,i):
            numbers[j] = False

    for j in range(2,n+1):
        if numbers[j] == True:
            cnt+=1

    return cnt