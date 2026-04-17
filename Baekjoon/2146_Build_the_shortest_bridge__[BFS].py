import sys
from collections import deque

DIR = [(0, -1), (1, 0), (0, 1), (-1, 0)]
def solution():
    N = int(sys.stdin.readline())
    wm = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # 각 섬별로 그룹핑(bfs)
    isl_id = -1 # 각 섬의 id 를 음수로 표현(섬, 바다가 양의 정수로 입력되므로) -> wm 을 바로 업데이트하므로 visited 따로 필요 없음.
    ports = set()
    for r in range(N):
        for c in range(N):
            if wm[r][c] <= 0: # 이미 섬으로 그루핑된 지역 탐색은 건너뛰기
                continue

            # 탐색 출발점 초기화
            q = deque([(r, c)])
            wm[r][c] = isl_id
            while q:
                cr, cc = q.popleft() # 현재 위치
                for dr, dc in DIR:
                    nr = cr+dr
                    nc = cc+dc
                    
                    # 처음 방문하는 섬만 그루핑
                    if 0 <= nr < N and 0 <= nc < N and wm[nr][nc] >= 0:
                        if wm[nr][nc] > 0: # 섬이면 id 업데이트
                            wm[nr][nc] = isl_id
                            q.append((nr, nc)) # 현재 위치와 인접하면서 값이 0보다 큰 좌표만 push 하므로 자연스럽게 인접한 섬만 그루핑할 수 있음.
                        
                        if wm[nr][nc] == 0:# 인접구역이 바다면 ports에 push
                            ports.add((cr, cc))

            isl_id -= 1
    
    # 가장 짧은 다리 찾기 (bfs)
    shortest_dist = sys.maxsize
    
    for pr, pc in ports:
        visited = [[False]*N for _ in range(N)]
        visited[pr][pc] = True
        dist = -1
        arrival = False
        curr_isl = wm[pr][pc]

        # 최초: 현재 거리(dist) 내에서 탐색 가능한 위치(1)만 저장 -> 탐색 도중: 현재 거리 내에서  탐색 가능한 위치 + 다음 거리(dist+1) 내에서 탐색 가능한 위치
        q = deque([(pr, pc)])
        while q:
            dist += 1

            # 현재 거리 내에서 탐색 가능한 위치만 pop되므로 이 loop을 탈출하면 q에 남게 되는 위치는 다음 거리 내에서 탐색 가능한 위치만 남게 됨.
            for _ in range(len(q)):
                cr, cc = q.popleft()
                for dc, dr in DIR:
                    nr = cr + dr
                    nc = cc + dc

                    # 현재 섬과 다른 영역인지 확인
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and wm[nr][nc] != curr_isl:
                        
                        # 다음 탐색 지점이 다른 섬일 경우
                        if wm[nr][nc] < 0:
                            arrival = True
                            shortest_dist = min(shortest_dist, dist)
                            break

                        # 바다일 경우
                        else:
                            q.append((nr, nc))
                            visited[nr][nc] = True

                if arrival: # loop 를 한 번 더 탈출하기 위해
                    break

    sys.stdout.write(f"{shortest_dist}")

solution()