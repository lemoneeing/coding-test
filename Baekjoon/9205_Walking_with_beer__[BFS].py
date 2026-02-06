MAX_BEER = 20
MOVE_LIMIT = 50

def calculate_Manhattan_distance(r0, c0, r1, c1):
    return abs(r1 - r0) + abs(c1 - c0)

# 그리디 방식 - 잘못된 풀이
# def solve():
#     tc = int(input().strip())
#     for _ in range(tc):
#         store_cnt = int(input().strip())
#         coordinates = [] # 집, 편, 행사장

#         for __ in range(store_cnt+2):
#             coordinates.append(list(map(int, input().split())))
        
#         coord_stores = coordinates[1:store_cnt+1] # 편의점 모음
#         fr, fc = coordinates[-1]
#         '''
#         ?집 ~ 행 총 거리 구한다?
        
#         현재 소유 맥주 수 = 초기화 20
        
#         현재 위치 ~ 남은 편 거리 구하기
#             현재 맥주로 "도달 가능한" 모든 편 구하기 -> 이 때 발견된 편 체크
#                 없으면 return sad
#                 있으면 가장 먼 거리의 편 선택
#             현재 위치 = 지금 편 초기화
#         '''

#         curr_beer = MAX_BEER    # 현재 맥주 초기화
#         cr, cc = coordinates[0] # 현재 위치 초기화
#         while True:
#             player_to_festival = abs(fr - cr) + abs(fc - cc)
#             if player_to_festival // MOVE_LIMIT <= curr_beer:
#                 print("happy")
#                 break

#             farthest_store = 0
#             farthest_store_idx = 0

#             for i, (sr, sc) in enumerate(coord_stores):
#                 store_to_festival = abs(fr - sr) + abs(fc - sc) # 편 ~ 행 거리
                
#                 if store_to_festival > player_to_festival: # 상 ~ 행 보다 편 ~ 행이 더 멀면 굳이 갈 필요 X
#                     continue

#                 player_to_store = abs(sr - cr) + abs(sc-cc) # 갈 수 있는 편의점
#                 need_beer = player_to_store // MOVE_LIMIT   # 편의점까지 필요한 맥주 수량
#                 if need_beer <= curr_beer: # 편의점까지 맥주 충분한지 검사
#                         farthest_store_idx = i
#                         farthest_store = player_to_store

#             if farthest_store == 0:
#                 print('sad')
#                 break

#             cr, cc = coord_stores.pop(farthest_store_idx)
#             curr_beer = MAX_BEER

from collections import deque

MAX_ALLOWED_DIST = 1000
def solve():
    tc = int(input().strip())
    for _ in range(tc):
        store_cnt = int(input().strip())

        player_q = deque([list(map(int, input().split()))]) # 상근이 좌표

        stores = [] # 집, 편, 행사장
        for __ in range(store_cnt):
            stores.append(list(map(int, input().split())))
        visited = [False] * store_cnt
        
        fr, fc = map(int, input().split()) # 행사장 좌표

        to_be_happy = False
        while player_q:
            pr, pc = player_q.popleft()
            if calculate_Manhattan_distance(pr, pc, fr, fc) <= MAX_ALLOWED_DIST:
                to_be_happy = True
                break

            for i, (sr, sc) in enumerate(stores):
                if not visited[i] and calculate_Manhattan_distance(pr, pc, sr, sc) <= MAX_ALLOWED_DIST:
                    player_q.append([sr, sc])
                    visited[i] = True

        if to_be_happy:
            print("happy")
        else:
            print("sad")

solve()       