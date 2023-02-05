def solution(keyinput, board):
    directions = {"up": [0, 1],"down": [0, -1],"left": [-1, 0],"right": [1, 0]}

    x = y = 0
    for i in keyinput:
        dx, dy = directions[i]
        nx, ny = x + dx, y + dy
        if abs(nx) <= ((board[0] - 1) // 2) and abs(ny) <= ((board[1] - 1) // 2):
            x, y = nx, ny

    return [x, y]

# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/120861
