import sys
def solution():
    N = int(sys.stdin.readline())
    stairs = [int(sys.stdin.readline()) for _ in range(N)]
    values = [[] for _ in stairs]
    
    values[0] = (stairs[0], 0)
    
    if N > 1:
        values[1] = (values[0][0]+stairs[1], stairs[1])
        
        for i in range(2, N):
            values[i] = (values[i-1][1]+stairs[i], max(values[i-2])+stairs[i])
        
    sys.stdout.write(f"{max(values[N-1])}")

solution()