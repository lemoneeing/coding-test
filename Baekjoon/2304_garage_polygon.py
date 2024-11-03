# import sys

# def solution():
#     N = int(sys.stdin.readline())
#     cols = []
#     last_pos = 0

#     for _ in range(N):
#         col = list(map(int, sys.stdin.readline().strip().split()))
#         last_pos = max(last_pos, col[0])
#         cols.append(col)
    
#     # 높이 값으로 정렬 
#     cols.sort(key=lambda x: x[1] * -1)
#     ans = [0] * (last_pos + 1)
#     ans[cols[0][0]] = cols[0][1] # 가장 높은 기둥만큼의 창고 면적 추가
    
#     # 가장 높은 기둥 기준으로 좌우로 그 다음 높은 기둥까지의 면적 확정
#     right_pivot = cols[0][0]
#     left_pivot = cols[0][0]
#     for col in cols[1:]:
#         curr_pos = col[0]
#         curr_height = col[1]
#         if curr_pos < left_pivot:
#             ans[curr_pos:left_pivot] = [curr_height] * (left_pivot -curr_pos)
#             left_pivot = curr_pos
#         elif curr_pos > right_pivot:
#             ans[right_pivot+1:curr_pos+1] = [curr_height] * (curr_pos - right_pivot)
#             right_pivot = curr_pos
        
#     sys.stdout.write(f"{sum(ans)}")
    
# solution()

import sys
input = sys.stdin.readline

n = int(input())

lhs = [0 for _ in range(1001)]
for _ in range(n):
    l, h = map(int, input().split())
    lhs[l] = h
max_idx = lhs.index(max(lhs))

max_val = 0
for i in range(max_idx):
    max_val = max(max_val, lhs[i])
    lhs[i] = max_val

max_val = 0
for i in range(1000, max_idx, -1):
    max_val = max(max_val, lhs[i])
    lhs[i] = max_val

print(sum(lhs))