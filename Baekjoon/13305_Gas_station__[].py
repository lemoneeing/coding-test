import sys

def solution():
    N = int(sys.stdin.readline())
    d = list(map(int, sys.stdin.readline().split()))
    c = list(map(int, sys.stdin.readline().split()))
    
    ans = 0
    curr = 0
    # 처음 출발할 땐 무조건 cost[0] * dist[0] 을 더함.
    ans += c[curr] * d[curr]
    chpst = c[curr]
    while curr < N - 2:
        next = curr + 1
        if c[next] < chpst:
            chpst = c[next]
            ans += c[next] * d[next] 
            
        else:
            ans += chpst * d[next]
        curr = next
    
    sys.stdout.write(f"{ans}")

solution()