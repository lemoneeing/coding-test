import sys
from collections import deque

input = sys.stdin.readline

def solve():
    N, M, K = map(int, input().split())
    GRID = [list(input().strip()) for _ in range(N)]

    broken = [[K+1] * M for _ in range(N)] # broken_walls[r][c]: (r, c) 까지 도달하기위해 부순 벽의 최소 수
    
    DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    q = deque([(0, 0, 0, 1)]) # k, r, c, dist
    while q:
        k, r, c, curr_dist = q.popleft()
        if r == N-1 and c == M-1: # 조기 종료
            print(curr_dist)
            return
        
        # 사방면 탐색
        for dr, dc in DIR:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < M:
                
                nk = k + 1 if GRID[nr][nc] == '1' else k

                # BFS 의 특성 상 먼저 도달한 거리가 가장 최소이므로 따로 최소 거리를 확인할 필요는 없음. 
                # 단, 동일한 거리일 때 파괴한 벽의 수가 더 적은 것이 더 유리한 조건이므로 그 때만 확인하여 갱신. 
                if nk <= K and broken[nr][nc] > nk: 
                    broken[nr][nc] = nk
                
                    q.append((nk, nr, nc, curr_dist + 1))
    
    print(-1)
    
solve()