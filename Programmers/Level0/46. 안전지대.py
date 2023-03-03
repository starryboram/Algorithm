def solution(board):
    N = len(board)
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    booms = [(x,y) for x in range(N) for y in range(N) if board[x][y] == 1]

    for x, y in booms:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny] = 1

    count = 0
    for x in range(N):
        for y in range(N):
            if board[x][y] == 0:
                count += 1

    return count

# 다시 풀어보기
# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/120866