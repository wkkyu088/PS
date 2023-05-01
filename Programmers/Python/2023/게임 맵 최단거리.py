from collections import deque

def solution(maps):
    max_x, max_y = len(maps), len(maps[0])
    queue = deque([(0, 0, 1)])
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    while queue:
        x, y, cnt = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == max_x-1 and ny == max_y-1:
                return cnt + 1
            if 0 <= nx < max_x and 0 <= ny < max_y:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = 0
                    queue.append([nx, ny, cnt+1])
    return -1