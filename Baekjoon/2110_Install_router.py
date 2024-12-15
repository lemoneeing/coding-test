import sys
input = sys.stdin.readline

def solution():
    H, R = map(int, input().strip().split())
    houses = []
    for _ in range(H):
        houses.append(int(input().strip()))
    houses.sort()
    print(houses)

    # 공유기를 최대한 멀리 설치
    #   - 집 위치가 최대한 중앙인 곳 위주로 설치
    #   - 개수가 R 이 될 때까지 범위를 절반씩 줄여 나가기 
    # 설치된 공유기 중 가장 가까운 거리 찾기
    #   - 마지막 라우 때 설치한 위치과 s, e 와의 거리 
    
    # installed = []
    # adj = []
    # longest = 0
    # def install(s, e, cnt):
    #     nonlocal R, houses, installed, longest

    #     if cnt == R:
    #         return

    #     if installable:
    #         if installed:
    #             currDist = abs(installed[-1] - houses[idx])
    #             if currDist > longest:
    #                 longest = currDist

    #         installed.append(houses[idx])

    #     return max(install(idx + 1, True), install(idx + 1, False)))

    # for h in houses:
    #     install(h)
    #     install()


    # 이분 탐색을 사용한 방법
    # 최소거리를 기준으로 설치할 수 있는 router 의 개수를 파악
    installed = 0
    adjDist = []
    start = 0
    end = H
    dist = houses[(houses[start] + houses[end] // 2)]
    while start < end:
        print(f"[ dist: {dist} ]")
        
        prevH = 0
        installed += 1
        print(f"install at :{houses[prevH]}")
        for currH in range(prevH+1, H):
                
            realDist = houses[currH] - houses[prevH] 
            if (realDist >= dist):
                print(f"install at :{houses[currH]}")
                
                installed += 1
                
                if prevH == 0:
                    realMinimumDist = houses[currH] - houses[prevH] 
                else:
                    realMinimumDist = min(realMinimumDist, realDist)
                prevH = currH
        
            if installed >=  R:
                print(f"Arrive router count.")
                adjDist.append(realMinimumDist)
                start += 1
                break
            
        if installed < R:
            end -= 1
        
        installed = 0
    
    print(max(adjDist))
        
solution()
            
                            
            
            
        
