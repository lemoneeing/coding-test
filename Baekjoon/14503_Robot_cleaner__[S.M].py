import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    sr, sc, d = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(N)]

    '''
    1.  현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    2.  현재 칸의 주변 $4$칸 중 청소되지 않은 빈 칸이 없는 경우,
        2-1 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        2-2 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
    3.  현재 칸의 주변 $4$칸 중 청소되지 않은 빈 칸이 있는 경우,
        3-1 반시계 방향으로 $90^\circ$ 회전한다.
        3-2 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
        3-3 1번으로 돌아간다.
        
    $0$인 경우 북쪽, 
    $1$인 경우 동쪽, 
    $2$인 경우 남쪽, 
    $3$인 경우 서쪽
    '''

    ans = 0
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    q = [(sr, sc)]
    while q:
        r, c = q.pop(0)
        if room[r][c] == 0:
            ans += 1
            room[r][c] = -1

        # 주변 4칸 탐색
        already_clean = 0
        for i in range(d, d-4, -1):
            nd = (i+3)%4
            dr, dc = dir[nd]
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M:
                # 주변에 청소되지 않은 빈 칸이 있는 경우
                if room[nr][nc] == 0:
                    q.append((nr, nc))
                    d = nd
                    break
                else:
                    already_clean += 1

        # 주변에 청소되지 않은 빈 칸이 있는 경우
        if already_clean == 4:
            # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            dr, dc = dir[(d+2)%4]
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if room[nr][nc] != 1:
                    q.append((nr, nc))
                else:
                    break

    sys.stdout.write(f"{ans}")

solution()
