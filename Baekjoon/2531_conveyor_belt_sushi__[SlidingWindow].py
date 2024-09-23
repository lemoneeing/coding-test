import sys

def solution():
    N, d, k, c = map(int, sys.stdin.readline().strip().split())
    belt = [int(sys.stdin.readline().strip()) for _ in range(N)]
    belt.extend(belt[:k-1])
    
# 자체 풀이 2704ms
    # belt[s:e] 에서 c 를 제외한 요소의 가짓수 중 가장 큰 것 찾기
    # ans = 0
    # for s in range(N):
    #     meal = set(belt[s:s+k])
    #     if c not in meal:
    #         ans = max(ans, len(meal)+1)
    #     else:
    #         ans = max(ans, len(meal))
        
# 참고 풀이
    eat = [0] * (d+1)
    currVrt = 0
    canUseCoupon = True
    for i in range(k):
        if eat[belt[i]] == 0:
            currVrt += 1
            if belt[i] == c:
                canUseCoupon = False
        eat[belt[i]] += 1
        
    currVrt = currVrt + 1 if canUseCoupon else currVrt
    
    ans = currVrt
    if canUseCoupon:
        currVrt -= 1
        
    for j in range(1, N):
        firstSshi = belt[j-1]
        if eat[firstSshi] == 1:
            currVrt -= 1
            if firstSshi == c:
                canUseCoupon = True
        eat[firstSshi] -= 1
        
        
        lastSshi = belt[j+k-1]
        if eat[lastSshi] == 0:
            currVrt += 1
            if lastSshi == c:
                canUseCoupon = False
        eat[lastSshi] += 1
        
        ans = max(ans, currVrt + 1 if canUseCoupon else currVrt)
        
    sys.stdout.write(f"{ans}")
    
solution()