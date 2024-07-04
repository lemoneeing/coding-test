def solution(n, times):
    s = 1
    e = min(times) * n
    
    while s <= e:
        mid = (s + e) // 2
        
        cnt = 0
        for time in times:
            cnt += mid // time
        
        if cnt < n:
            s = mid + 1
        else:
            e = mid - 1
            
    return s

# print(solution(6, [7, 10]))
# print(solution(1, [7]))
# print(solution(59, [1, 1]))
print(solution(3, [1, 1]))