# https://school.programmers.co.kr/learn/courses/30/lessons/120861?language=python3#
def solution(keyinput, board):
    lim_x, lim_y = board[0]//2, board[1]//2
    
    move = {'left': (-1, 0), 'right': (1, 0), 'up':(0, 1), 'down':(0, -1)}
    x, y = 0, 0
    for k in keyinput:
        dx, dy = move[k]
        if abs(x+dx) > lim_x or abs(y+dy) > lim_y:
            continue
        else:
            x, y = x+dx, y+dy
    return [x, y]