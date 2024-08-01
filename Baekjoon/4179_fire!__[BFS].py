import sys

def solution():
    
    R, C = map(int, sys.stdin.readline().split())
    
    fire_path = []
    player_path = []
    maze = []
    
    f_q = []
    for r in range(R):
        maze.append(list(sys.stdin.readline())) 
        fire_path.append([])
        player_path.append([])
        
        for c in range(C):
            fire_path[r].append(sys.maxsize)
            player_path[r].append(sys.maxsize)
            
            if maze[r][c] == 'F':
                fire_path[r][c] = 0
                f_q.append((r, c))
                
            if maze[r][c] == 'J':
                player_path[r][c] = 0
    
    dx = (0, 1, 0, -1)
    dy = (-1, 0, 1, 0)
    
    while f_q:
        curr_f = f_q.pop(0)
        
        for off_x, off_y in zip(dx, dy):
            if maze[curr_f[0]+off_x][curr_f[1]+off_y] < sys.maxsize:
                continue
            
    
solution()