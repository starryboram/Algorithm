n = int(input()) # 움직일 횟수 입력받기
x, y = 1, 1
move = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_type = ['L','R','U','D']

for m in move: # 입력에 의한 움직임
    for i in range(len(move_type)):
        if m == move_type[i]: # 입력이 L,R,U,D 일 때
            mx = x + dx[i] 
            my = y + dy[i]

    if mx < 1 or my <1 or mx > n or my > n: # 공간 벗어날 때
        continue # 그냥 무시
    
    x, y = mx, my # 식에 의해 이동

print(x, y)

# 다시 한 번 풀어보기