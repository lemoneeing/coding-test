import sys

# 시간 초과
# def solution():
    # ans = 0
    
    # N, K = map(int, sys.stdin.readline().strip().split())
    # arr = list(sys.stdin.readline().strip())
    # ham = []
    # per = []
    # for i, c in enumerate(arr):
    #     if c == 'H':
    #        ham.append(i)
    #     elif c == 'P':
    #         per.append(i)
            
    # for p in per:
    #     del_target = []
    #     for h in ham:
    #         if p-K <= h <= p+K:
    #             ans+=1
    #             del_target.append(h)
    #             break
    #         if h < p:
    #             del_target.append(h)
    #     for dt in del_target:
    #         ham.remove(dt)
    
    # sys.stdout.write(f"{ans}")

def solution():
    ans = 0
    
    N, K = map(int, sys.stdin.readline().strip().split())
    arr = list(sys.stdin.readline().strip())
    for p, c in enumerate(arr):
        if c == 'P':
            s = p - K if p >= K else 0
            e = p + K if p < N - K else N - 1
            for h in range(s, e+1):
                if arr[h] == 'H':
                    ans += 1
                    arr[h] = ''
                    break
                
    sys.stdout.write(f"{ans}")
    
solution()