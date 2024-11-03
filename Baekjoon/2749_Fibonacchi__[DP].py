import sys
input = sys.stdin.readline

def solution():
    N = int(input().strip())
    
    fib = [0, 1] 
    
    for i in range(2, N+1):
        fib.append(fib[0] + fib[1])
        fib = fib[1:]
        
    sys.stdout.write(f"{fib[-1] % 1000000}")
    
solution()