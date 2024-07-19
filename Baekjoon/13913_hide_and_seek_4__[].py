import sys

def solution():
    s, e = map(int, sys.stdin.readline().split())
    # s = 3, e = 11
    # 11 <- 10 <- 5 <- 4 <- 2 <- 1 <- 0     # e 에서 탐색 시작. 다음 점은 -= 1, +=1, /=2 했을 때 보다 크고 v[i] = False 인 값
    #                         <- 3 (!)
    #                    <- 3 (!)           # 현재 depth 가 더 짧으면 갱신
    #               <- 6 <- 3 (!)
    #                    <- 7 <- 8 <- 4
    #          <- 9 <- 8 <- 7 <- 6 ...
    #    <- 12 <- 6 <- 3 (!)
    #          <-13 <-14 <-15 ......
    
    # 11 에서 갈 수 있는 경로 : 10, 12, 22 -> p[10], p[12], p[22]
    # 갈 수 있는 경로 :       0  1  2   3  4  5  6  7  8  9 10 11 12 13 14 15 16 .....22
    # 0 -> 최단 경로: p[0] = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    # 1 -> 최단 경로: p[1] = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0
    # 2 -> :          p[2] = [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0
    # 3 -> :          p[3] = [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0
    # 4 -> :          p[4] = [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0
    # 5 -> :          p[5] = [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0
    # 6 -> :          p[6] = [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1
    # 7 -> :          p[7] = [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1
    # 8 -> :          p[8] = [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1
    
    p[0][1] = [0, 1]
    p[0][2] = set(p[0][1] + p[1][2]]
    p[0][3] = set(p[0][2] + p[2][3]])
    ...
    p[1][0] = set(1, 0)
    p[1][2] = set(1, 2)
    p[1][3] = set(p[1][2] + p[2][3])
    p[1][4] = set(p[1][2] + p[2][4])
    p[1][5] = p[1][2] + min(set(p[2][3] + p[3][4] + p[4][5]), set(p[2][4] + [4][5]))
    
    
    possible = [[] for _ in range(e * 2 + 1)]
    
    def dp(curr):
        nonlocal possible
        
        if v[curr]:
            return ''
            
        if curr == s :
            return curr
        
        v[curr] = True
        
        for i in range(e * 2 + 1):
            if e % 2 == 0:
                # 
            
    
    
    def find_shortest_path(*paths):
        nonlocal s
        
        minL = sys.maxsize
        shst = ''
        
        for p in paths:
            if len(p) == 0 or not p.__contains__(f" {s}"):
                continue
            
            if len(p) < minL:
                shst = p
                minL = len(shst)
        return shst
    
    best = ''
    def go_next(curr, path):
        nonlocal v, s, best
        
        if curr == s:
            path += f"{curr}"
            v[curr] = True
            return path
        elif curr == 0 and not v[0]:
            path += f"{curr} "
            return path
        elif v[curr]:
            return path
        elif len(path) > len(best) > 0:
            return ''
        
        path += f"{curr} "
        v[curr] = True
        
        db_path = ''
        if curr % 2 == 0:
            db_path = go_next(curr//2, path)
            v[curr//2] = False
            
        bwd_path = go_next(curr-1, path)
        v[curr-1] = False
        
        fwd_path = go_next(curr+1, path)
        v[curr+1] = False
        
        res = find_shortest_path(best, db_path, bwd_path, fwd_path)
        if res:
            best = res
        return best
    
    v = [False for _ in range(max(s, e)*2)]
    return go_next(e, '')
    
print(solution())