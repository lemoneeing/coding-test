def solve():

    N, L = map(int, input().split())
    puddles = [list(map(int, input().split())) for _ in range(N)]
    puddles.sort()
    
    ans = 0

    last_repaired_pos = 0
    '''
    웅덩이 순회
        if pe < last_repaired_pos: # 마지막 웅덩이 끝 이미 수리 완료 
            시작점 = last_repaired_pos
        else:
            시작점 = 첫 웅덩이 시작점
            
        last_repaired_pos = 시작점 + L
        ans += 1
        
        if pe <= last_repaired_pos: # 현재 웅덩이 수리 완료
            break
        else:
            while pe <= last:
                시작점 = last
                last = 시작점 + L
    '''

    for ps, pe in puddles:
        curr = max(ps, last_repaired_pos)

        puddle_size = pe - curr
        cnt = puddle_size // L if puddle_size % L == 0 else puddle_size // L + 1
        last_repaired_pos = curr + (L * cnt)
        ans += cnt

    print(ans)

solve()