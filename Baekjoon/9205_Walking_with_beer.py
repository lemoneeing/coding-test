MAX_BEER = 20
MOVE_LIMIT = 50

def calculate_Manhattan_distance(r0, c0, r1, c1):
    return abs(r1 - r0) + abs(c1 - c0)

def solve():
    tc = int(input().strip())
    for _ in range(tc):
        store_cnt = int(input().strip())
        coordinates = [] # 집, 편, 행사장

        for __ in range(store_cnt+2):
            coordinates.append(list(map(int, input().split())))
        
        coord_stores = coordinates[1:store_cnt+1] # 편의점 모음
        
        '''
        ?집 ~ 행 총 거리 구한다?
        
        현재 소유 맥주 수 = 초기화 20
        
        현재 위치 ~ 남은 편 거리 구하기
            현재 맥주로 "도달 가능한" 모든 편 구하기 -> 이 때 발견된 편 체크
                없으면 return sad
                있으면 가장 먼 거리의 편 선택
            현재 위치 = 지금 편 초기화
        '''

        curr_beer = MAX_BEER    # 현재 맥주 초기화
        cr, cc = coordinates[0] # 현재 위치 초기화

        while True: # TODO 
