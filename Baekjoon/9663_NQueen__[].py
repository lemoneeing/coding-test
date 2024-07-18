import sys
    
def backtracking(row):
    global N, ans, board, v1, v2, v3
    
    if row == N:
        return ans
        
    i = row
    for j in range(N):
        if i == 0:
            board[i][j] = 1
        else:
            if v1[j] == v2[] == v3[] == 0:
                board[row][c] = 1
                break
        

        
    return ans

def solution(n):
    N = n
    # N = int(sys.stdin.readline().strip())
    ans = 0
    
    board = [[0 for _ in range(N)] for __ in range(N)]
    

    v1 = [0 for _ in range(row)] # 상
    v2 = [] # 좌 상
    v3 = [] # 우 상
    
    for row in range(N):
        sys.stdout.writh(f"{backtracking(row)}")


solution(3)
