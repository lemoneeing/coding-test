import sys
import copy

def solution():
    N = int(sys.stdin.readline())
    wm = []
    # visited = []
    for _ in range(N):
        wm.append(list(map(int, sys.stdin.readline().split())))
        # visited.append([False for __ in range(N)])

    dx = (0, 1, 0, -1)
    dy = (-1, 0, 1, 0)
    ports = [] # 각 섬의 끝에 위치한 타일들의 좌표

    # 각 섬마다 id 부여하여 구분짓기 + 다리 시작점 찾기(bfs)
    isl_id = -1
    for r in range(N):
        for c in range(N):
            if wm[r][c] <= 0:
                continue
            q = [(r, c)]
            while q:
                curr = q.pop(0)
                for x, y in zip(dx, dy):
                    nx_r = curr[0]+y
                    nx_c = curr[1]+x
                    if 0 <= nx_r < N and 0 <= nx_c < N:
                        if wm[nx_r][nx_c] > 0 and (nx_r, nx_c) not in q:
                            q.append((nx_r, nx_c)) # q 에는 0 보다 큰 타일의 좌표만 저장됨. 
                        elif wm[nx_r][nx_c] == 0 and (curr[0], curr[1]) not in ports: # 옆 타일이 하나라도 바다(0) 이면 port 타일임.
                            ports.append((curr[0], curr[1]))
                            
                wm[curr[0]][curr[1]] = isl_id

            isl_id -= 1

    # 가장 짧은 다리 찾기 (bfs)
    shortest_br = sys.maxsize
    for port in ports:
        tmp_m = [copy.deepcopy(e) for e in wm]
        
        find = False
        br_q = [port]
        while br_q and not find:
            c_port = br_q.pop(0)
            for x, y in zip(dx, dy):
                nx_r = c_port[0]+y
                nx_c = c_port[1]+x
                
                # 지도 안에 있는 좌표만 검사
                if 0 <= nx_r < N and 0 <= nx_c < N:
                    # 바다이면 다리 짓기
                    if tmp_m[nx_r][nx_c] == 0:
                        tmp_m[nx_r][nx_c] = 1 if c_port in ports else tmp_m[c_port[0]][c_port[1]] + 1
                        if (nx_r, nx_c) not in br_q:
                            br_q.append((nx_r, nx_c))

                    # 다른 섬에 도달 = 해당 port 에서 지을 수 있는 가장 짧은 다리
                    elif tmp_m[nx_r][nx_c] < 0 and tmp_m[nx_r][nx_c] != tmp_m[port[0]][port[1]]:
                        shortest_br = min(tmp_m[c_port[0]][c_port[1]], shortest_br)
                        find = True
                        break

    if shortest_br < sys.maxsize:
        sys.stdout.write(f"{shortest_br}")
    else:
        sys.stdout.write(f"INF")

solution()