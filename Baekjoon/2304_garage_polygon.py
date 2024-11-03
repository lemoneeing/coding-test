import sys

def solution():
    N = int(sys.stdin.readline())
    cols = []
    for _ in range(N):
        cols.append(tuple(map(int, sys.stdin.readline().strip().split()))) 
        
    print(cols)
    
solution()