n = input() # 입력이 주어지고
sum = 0 # 전체 값을 셋팅함

for i in range(len(n)//2): # 0 ~ len(n)/2까지 돌아가면서
    sum += int(n[i]) # 해당 값을 더해줌
for j in range(len(n)//2, len(n)): #len(n)/2 ~ len(n)까지 돌아가면서
    sum -= int(n[i]) # 해당 값을 빼줌

if sum == 0: # 합이 0이라는건: 왼쪽 오른쪽의 합이 같다.
    print("LUCKY")
else: # 합이 0이 아니라는 건: 왼쪽, 오른쪽의 합이 다르다.
    print("READY")