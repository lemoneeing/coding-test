import sys
input = sys.stdin.readline

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def widen(grid, p, catle_areas, moving_count):
    '''
    catle_areas[p] 좌표들을 시작점으로 moving_count만큼 bfs 탐색 시작

    areas = deepcopy(catle_areas)
    for r, c in areas:
        # r, c 방문처리 -> c.a 에서 제거?
        # for grid[r][c] 기준으로 상하좌우 탐색   
        #   for _ in range(moving_count):
        #       이동 = r,c + dr, dc
        #       이동할 수 없으면 
        #           현재 r, c 를 catle_areas 에서 제거
        #       이동가능하면 
        #           grid 업데이트
        #           catle_areas 에 append
        

    
    :param grid: Description
    :param p: Description
    :param catle_area_list: Description
    '''


def solve():
    N, M, P = map(int, input().split())
    moving_cells = list(map(int, input().split()))
    grid = [list(input().strip()) for _ in range(N)]

    for r in range(N):
        for c in range(M):
            grid[r][c]