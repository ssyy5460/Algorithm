from collections import deque
def bfs(maps):
    n = len(maps)
    m = len(maps[0])
    
    if n == 1 and m == 1:
        return 1
    
    ans = 0
    queue = deque()
    queue.append([0,0])
                
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<=ny< m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append([nx,ny])
    return maps[-1][-1]

def solution(maps):
    answer = 0
    
    if bfs(maps) == 1:
        answer -= 1
    else:
        answer = bfs(maps)
    return answer
    

                
