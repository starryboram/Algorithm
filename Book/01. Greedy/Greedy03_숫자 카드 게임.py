n,m = map(int, input().split()) # n * m 입력받기
answer = 0

for i in  range(n):
    data = list(map(int, input.split())) # 숫자 카드 입력받기

    min_i = min(data) # 가장 작은 숫자 찾기
    answer = max(answer, min_i) # 여기서 가장 큰 수 찾기

print(answer)