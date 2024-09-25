import sys

def solution():
    q = 0
    N = int(sys.stdin.readline().strip())
    ans = []
    while N > 0:
        q += 1
        cave = []
        ps = []
        for _ in range(N):
            cave.append(list(map(int, sys.stdin.readline().strip().split())))
            ps.append([0 for _ in range(N)])
        
        # 
        # 5 5 4
        # 3 9 1
        # 3 2 7
        # 1)
        # 1-1) r == 0 
        #   ps[r][c] = ps[r][c-1] + c[r][c]
        # 1-2) c == 0
        #   ps[r][c] = ps[r-1][c] + c[r][c]
        # 5 10 0 
        # 8 0  0
        # 0 0  0
        #
        # 2) r > 0 and c > 0 
        #   ps[r][c] = min(ps[r][c-1] + c[r][c], ps[r-1][c] + r[r][c])
        # 5 10 14 
        # 8 min(17, 19), 0
        # 11, 0, 0
        #
        # 3) 
        # 5  10              14
        # 8  17              min(17, 14) + 1
        # 11 min(11, 17) + 2 0
        # 4)
        # 5 10 14
        # 8 17 15
        # 11 13 min(13, 15) + 7
        
        for r in range(0, N):
            for c in range(0, N):
                if r == 0 and c == 0:
                    ps[r][c] = cave[r][c]
                    continue
                
                if r == 0:
                    ps[r][c] = ps[r][c-1] + cave[r][c]
                elif c == 0:
                    ps[r][c] = ps[r-1][c] + cave[r][c]
                else:
                    ps[r][c] = min(ps[r][c-1], ps[r-1][c]) + cave[r][c]
        
        ans.append(str(ps[N-1][N-1]))
        
        N = int(sys.stdin.readline().strip())
    
    for i, a in enumerate(ans):
        sys.stdout.write(f"Problem {i+1}: {a}\n")
        
solution()