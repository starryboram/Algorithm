n,m,k = map(int,input().split()) # n,m,k를 공백으로 구분해서 입력받음
data = list(map(int, input().split()))

data.sort() # 데이터 작은수부터 정렬
answer = 0

while True:
    for i in range(k):
        if m == 0: # 반복문 탈출 조건(더할 수 있는 숫자 = m)
            break
        answer += data[-1] # 가장 큰 수 더해줌
        m -= 1 # 더할 때마다 1 빼줌

    if m == 0:
        break

    answer += data[-2] # 두 번째로 큰 수 더해줌
    m -= 1 # 다시 빼줌

print(answer)

##################### 더 심화(나동빈 강사) ######################
n,m,k = map(int,input().split()) # n,m,k를 공백으로 구분해서 입력받음
data = list(map(int, input().split()))
data.sort() # 데이터 작은수부터 정렬

# 가장 큰 수가 더해지는 횟수 계산
cnt = int(m/(k+1)) * k
cnt += m%(k+1)

answer = 0
answer += (cnt)*data[-1]
answer += (m-cnt)*data[-2]

print(answer)