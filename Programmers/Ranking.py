from queue import Queue

    # 방향 그래프, 위상정렬
    # 정확한 순위를 측정할 수 있음 = 위상정렬로 정렬될 수 있음.
    # adj = [[], [2], [5], [2], [2, 3], []]
def solution(n, results):
    answer = 0
    
    adj = [[] for _ in range(n+1)]
    d = [0] * (n+1)
    for w, l in results:    # 인접리스트 초기화
        adj[w].append(l)
    
    
    for i in range(1, n+1):
        for next in adj[i]:
            adj[i] = list(set(adj[i] + adj[next]))
    
    q = []
    for j, win in enumerate(adj):
        d[j] = len(win)
        if d[j] == 0:
            q.append(j)
            
    while q:
        curr = q[0]
        q.remove(curr)
        answer += 1
        
        for next in adj[curr]:
            if d[next] == 0:
                q.append[next]
            else:
                d[next] -= 1
        
        
    return answer

# print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
print(solution(5, [[1, 4], [4, 2], [2, 5], [5, 3]]))
    