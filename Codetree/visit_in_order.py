import sys

# DFS 재귀 깊이 제한 해제 (격자 크기가 커질 경우를 대비)
sys.setrecursionlimit(10 ** 6)
n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

target_positions = []
for _ in range(m):
    x, y = map(int, input().split())
    target_positions.append((x - 1, y - 1))


total_routes = 0

# 1. 방문 여부를 체크할 n x n 크기의 visited 배열 초기화
visited = [[False] * n for _ in range(n)]

# 3. 상하좌우 이동을 위한 방향 벡터 정의
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def solution(sr: int, sc: int, target_idx:int) -> int:
    """
    현재 좌표 (r, c)에서 target_idx번째 목적지를 향해 탐색하는 백트래킹 함수.
    """
    global total_routes
    
    # [목적지 도달 처리]
    # 현재 위치가 현재 추적 중인 목적지와 일치하는 경우
    if (sr, sc) == target_positions[target_idx]:
        # 만약 마지막 목적지까지 모두 순서대로 방문했다면 올바른 경로 1개 발견!
        if target_idx == m - 1:
            total_routes += 1
            return
        # 아직 방문할 목적지가 남았다면 다음 목적지 인덱스(target_idx + 1)로 넘어가서 계속 탐색
        else:
            target_idx += 1
    
    # 상하좌우 4방향 탐색
    for i in range(4):
        nr, nc = sr + dr[i], sc + dc[i]
        
        # 격자 범위를 벗어나면 제외
        if not (0 <= nr < n and 0 <= nc < n):
            continue
            
        # 이미 현재 경로에서 방문했으면 제외
        if visited[nr][nc]:
            continue
            
        # 격자 칸의 값이 1인 지역(장애물)이면 제외
        if grid[nr][nc] == 1:
            continue
            
        # [미래의 목적지 가지치기 규칙]
        # 아직 방문할 차례가 되지 않은 '미래의 목적지' 배열 추출
        future_targets = target_positions[target_idx + 1 :]
        # 다음에 이동할 칸이 미래의 목적지에 포함되어 있다면 해당 경로 차단
        if (nr, nc) in future_targets:
            continue
            
        # [백트래킹 전진 및 역추적]
        visited[nr][nc] = True  # 방문 표시
        solution(nr, nc, target_idx)  # 다음 칸 탐색 진행
        visited[nr][nc] = False # 방문 해제 (역추적 원상복구)

    return total_routes

visited[target_positions[0][0]][target_positions[0][1]] = True
print(solution(target_positions[0][0], target_positions[0][1], 1))