import sys
input = sys.stdin.readline

DIR = [(0, -1), (1, 0), (0, 1), (-1, 0)]
def solve():
    N, M = map(int, input().split())
    grid = [[0] * (N) for _ in range(N)]
    
    # 파종
    for _ in range(M):
        sr, sc, l, seed = map(int, input().split())
        for i in range(l):
            for j in range(l):
                grid[sr+i][sc+j] = seed

    # 과일 별 누적합 초기화
    fruits_cnt = [[[0] * (N+1) for _ in range(N+1)] for __ in range(8)] # fruits_cnt[f][r][c]: (0,0) ~ (r,c) 영역에서 과일 f 의 합
    for f in range(1, 8):
        for r in range(1, N+1):
            for c in range(1, N+1):
                val = 1 if grid[r-1][c-1] == f else 0
                fruits_cnt[f][r][c] = fruits_cnt[f][r-1][c] + fruits_cnt[f][r][c-1] - fruits_cnt[f][r-1][c-1] + val
    
    # 이분탐색
    low, high = 1, N
    ans = 0
    while low < high:
        mid = (low + high) //2
        is_available = False

        for r in range(N-mid+1):
            for c in range(N-mid+1):
                f_type_cnt = 0
                f_sum = 0

                if fruits_cnt[0][r+mid][c+mid] - fruits_cnt[0][r][c+mid] - fruits_cnt[0][r+mid][c] + fruits_cnt[0][r][c]:
                    continue

                for f in range(1, 8):
                    f_cnt = fruits_cnt[f][r+mid][c+mid] - fruits_cnt[f][r][c+mid] - fruits_cnt[f][r+mid][c] + fruits_cnt[f][r][c]
                    if f_cnt > 0: # 0번 씨앗 없음.
                        f_type_cnt += 1
                        f_sum += f_cnt
                
                if f_type_cnt <= 2 and f_sum == mid * mid:
                    ans = max(ans, mid)
                    is_available=True
                    break
        
        if is_available:
            low = mid+1
        else:
            high = mid
    
    print(ans*ans)

solve()    