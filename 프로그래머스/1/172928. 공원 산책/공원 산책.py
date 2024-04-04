def solution(park, routes):
    # 행
    n = len(park)
    
    # 열
    m = len(park[0])
    
    # 시작점 찾기
    start = [(i,j) for i in range(n) for j in range(m) if park[i][j] == 'S']
    
    x, y = int(start[0][0]), int(start[0][1])
    
    # 명령에 따라 이동
    for route in routes:
        # 방향, 거리
        direction, d = route.split(' ') 
        dist = int(d)
        
        if direction == 'E' and (y + dist <= m-1) : 
            for i in range(dist):
                if park[x][y+i+1] == 'X':
                    break
            else:
                y += dist
            
            
        elif direction == 'W' and (y - dist >= 0) :
            for i in range(dist):
                if park[x][y-i-1] == 'X':
                    break
            else:
                y -= dist
            
        elif direction == 'S' and (x + dist <= n-1) :
            for i in range(dist):
                if park[x+i+1][y] == 'X':
                    break
            else:
                x += dist
            
            
        elif direction == 'N' and (x - dist >= 0) :
            for i in range(dist):
                if (park[x-i-1][y] == 'X'):
                    break
            else:
                  x -= dist
    
    return [x,y]


    