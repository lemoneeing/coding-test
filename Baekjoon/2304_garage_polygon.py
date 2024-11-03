import sys

def solution():
    N = int(sys.stdin.readline())
    cols = []
    last_pos = 0

    for _ in range(N):
        col = list(map(int, sys.stdin.readline().strip().split()))
        last_pos = max(last_pos, col[0])
        cols.append(col)
    
    # 높이 값으로 정렬 
    cols.sort(key=lambda x: x[1] * -1)
    ans = [0] * (last_pos + 1)
    ans[cols[0][0]] = cols[0][1] # 가장 높은 기둥만큼의 창고 너비 추가
    
    # 가장 높은 기둥 기준으로 좌우로 그 다음 높은 기둥을 찾아 너비 구하기
    right_pivot = cols[0][0]
    left_pivot = cols[0][0]
    for col in cols[1:]:
        curr_pos = col[0]
        curr_height = col[1]
        if curr_pos < left_pivot:
            ans[curr_pos:left_pivot] = [curr_height] * (left_pivot -curr_pos)
            left_pivot = curr_pos
        elif curr_pos > right_pivot:
            ans[right_pivot+1:curr_pos+1] = [curr_height] * (curr_pos - right_pivot)
            right_pivot = curr_pos
        
    sys.stdout.write(f"{sum(ans)}")
    
solution()