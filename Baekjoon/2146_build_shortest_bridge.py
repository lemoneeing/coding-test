import sys

def solution():
    N = int(sys.stdin.readline())
    
    wm = []
    for _ in range(N):
        wm.append(list(map(int, sys.stdin.readline().split())))
    
    ports = []
    dir_type = []
    dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for r in range(N):
        for c in range(N):
            # 현재 칸의 <상 우 하 좌> 탐색하여 0 인 곳이 1개 이상인 지점 저장
            for i, d in enumerate(dir):
                if wm[r+d[0]][c+d[1]] == 0:
                    ports.append((r, c))
                    dir_type.append(i)
    
    # port 들끼리 연결
    curr = []
    brdg = 0
    for j, port in enumerate(ports):
        # <상우하좌> 반복 돌면서 0인 곳으로 쭉쭉 -> BFS
        [port[0]+dir[dir_type[j]][0], port[1]+dir[dir_type[j]][1]]
        def bfs(x, y, dpth):
            nonlocal ports, dir_type, dir, wm, brdg
            
            q = [(x, y)]
            while q:
                curr = q.pop(0)
                
                # 현재 위치가 목표지점이면 다리 길이 반환
                if curr in ports:
                    return dpth
                
                for d in dir:
                    next = (curr[0]+d[0], curr[1]+d[1])
                    
                    # 다음으로 이동할 수 있는 길 추가
                    if wm[next[0]][next[1]] == 0:
                        q.append(next)
                        wm[next[0]][next[1]] = 2
                        
                        bfs()
            # => 여기를 재귀로 만들어서 bfs 탐색하다가 port 만나면 재귀 끝내도록 + 깊이 기록
        
################################################# 여기까지 직접 작성함.




                    