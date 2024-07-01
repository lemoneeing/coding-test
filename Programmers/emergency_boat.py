# limit 을 2로 나눈 값을 기준으로 작은 무게와 큰 무게로 나눈 배열 구하기
# 작은 무게는 오름차순, 큰 무게는 내림차순으로 정렬
# 어느 한 배열이 끝날 때까지 반복
# 요소가 남은 배열이 작은 배열이면 2로 나누기
# 큰 배열이 남으면 남은 요소 개수만큼 더하기

def solution(people, limit):
    people.sort()
    crit = limit/2
    
    s_w = []
    h_w = []
    for w in people:
        if w <= crit:
            s_w.append(w)
        else:
            h_w.append(w)
    
    boat = 0
    hi=len(h_w)-1
    while s_w and h_w and hi >= 0:
        sw = s_w[0]
        hw = h_w[hi]
        
        if sw + hw <= limit:
            boat += 1
            s_w.pop(0)
            h_w.pop(hi)
        hi -= 1
            
        
    if s_w:
        if len(s_w) % 2 ==0:
            boat += int(len(s_w)/2)
        else:
            boat += (int(len(s_w)/2) + 1)
    
    if h_w:
        boat += len(h_w)
    
    return boat

# print(solution([40,55,55,60,60,70,80], 100))
print(solution([40,50,150,160], 200))


################################### 재도전
# def solution(people, limit):
#     people.sort()
#     boat = 0
#     s = 0
#     e = len(people) - 1
#     while s < e:
#         sw = people[s]
#         hw = people[e]
        
#         if sw + hw <= limit:
#             boat += 1
#             s += 1
#             e -= 1
#         else:
#             e -= 1
        
    
#     return boat

# print(solution([40,50,150,160], 200))