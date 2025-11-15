import sys
input = sys.stdin.readline

class Room:
    def __init__(self, room_id, pos_r, pos_c):
        self.id = room_id
        self.row = pos_r
        self.col = pos_c
        self.switches = []
        self.light_on = False

    def add_switches(self, target_r, target_c):
        self.switches.append((target_r, target_c))

def solution():
    N, M = map(int, input().split())
    light_grid = [[0] * (N+1) for _ in range(N+1)]      # 불 켜진 방 체크
    room_grid = [[None] * (N+1) for _ in range(N+1)]    # 스위치 있는 방 체크
    visit_grid = [[False] * (N+1) for _ in range(N+1)]  # 방문한 방 체크

    # 각 방의 스위치 초기화
    for i in range(M):
        r, c, s_r, s_c = map(int, input().split())
        if not room_grid[r][c]:
            room = Room(i, r, c)
        else:
            room = room_grid[r][c]
        room.add_switches(s_r, s_c)
        room_grid[r][c] = room


    ans = 1
    light_grid[1][1] = 1
    q = [(1,1)]
    visit_grid[1][1] = True
    while q:
        for _ in range(len(q)):
            curr_r, curr_c = q.pop(0)
            visit_grid[curr_r][curr_c] = True
            if room_grid[curr_r][curr_c]:
                # 현재 방에서 켤 수 있는 모든 방 켜기 -> 카운팅
                for sw_r, sw_c in room_grid[curr_r][curr_c].switches:
                    # 불 켜기
                    if not light_grid[sw_r][sw_c]:
                        ans += 1
                        light_grid[sw_r][sw_c] = 1
                        
                        # 불을 켠 방의 이동여부(=내가 방문'했던' 방과 인접한지) 체크
                        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                            ar_sw_r = sw_r + dr
                            ar_sw_c = sw_c + dc
                            if 1 <= ar_sw_r <= N and 1 <= ar_sw_c <= N and visit_grid[ar_sw_r][ar_sw_c] and (ar_sw_r, ar_sw_c) not in q:
                                q.append((sw_r, sw_c))
            
            # 현재 내가 방문한 방에서 이동 가능한 방(=불 켜짐 + 방문 전) 체크
            for dr, dc in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                ar_r = curr_r + dr
                ar_c = curr_c + dc
                if 1 <= ar_r <= N and 1 <= ar_c <= N and light_grid[ar_r][ar_c] and not visit_grid[ar_r][ar_c] and (ar_r, ar_c) not in q:
                    q.append((ar_r, ar_c))

    print(ans)

solution()