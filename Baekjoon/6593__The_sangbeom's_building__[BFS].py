import sys
from collections import deque

input = sys.stdin.readline

DIR = [(0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1), # 상 우 하 좌 
        (1, 0, 0), (-1, 0, 0)] # 윗층 아랫층
            

def solve():
    while True:
        line = input().strip()
        if not line:
            continue

        L, R, C= map(int, line.split())
        if L == 0 and R == 0 and C == 0:
            break
        
        building = [[]]
        start_pos = None
        exit_pos = None
        l = 0
        r = 0
        while r < R * L:
            floor = list(input().strip())
            if floor:
                building[-1].append(floor)

                try:
                    if start_pos is None:
                        # 'S' 가 있을 때
                        c = floor.index('S')
                        start_pos = (l, r%R, c)
                except ValueError:
                    pass

                try:
                    if exit_pos is None:
                        # 'E'가 있을 때
                        c = floor.index('E')
                        exit_pos = (l, r%R, c)
                except ValueError:
                    pass

                r += 1
                    
            else:
                building.append([])
                l += 1
        
        ans = 0
        spent = 0
        is_exit = False
        q = deque([start_pos])
        visited = [[[False] * C for _ in range(R)] for __ in range(L)]
        visited[start_pos[0]][start_pos[1]][start_pos[2]] = True
        while q:
            # curr_lev_adj_len = len(q)
            spent += 1
            for adj in range(len(q)):
                l, r, c = q.popleft()
                    
                for dl, dr, dc in DIR:
                    nl, nr, nc = l + dl, r + dr, c + dc
                    if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C and building[nl][nr][nc] != '#' and not visited[nl][nr][nc]:
                        if building[nl][nr][nc] == 'E':
                            ans = spent
                            is_exit = True
                            break

                        q.append((nl, nr, nc))
                        visited[nl][nr][nc] = True
                if is_exit:
                    break
            if is_exit:
                break

        if ans:
            sys.stdout.write(f"Escaped in {ans} minute(s).\n")
        else:
            sys.stdout.write("Trapped!\n")

solve()