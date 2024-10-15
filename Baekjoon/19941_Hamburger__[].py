import sys

# 시간 초과
def solution():
    ans = 0
    
    N, K = map(int, sys.stdin.readline().strip().split())
    arr = list(sys.stdin.readline().strip())
    ham = []
    per = []
    for i, c in enumerate(arr):
        if c == 'H':
           ham.append(i)
        elif c == 'P':
            per.append(i)
            
    for p in per:
        for h in ham:
            if p-K <= h <= p+K:
                ans+=1
                ham.remove(h)
                break
    
    sys.stdout.write(f"{ans}")
solution()