def solution(n, edge):

    answer = 0

    adj = [[] for _ in range(n+1)]
    for e in edge:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])

    dist = [5001] * (n+1)
    dist[1] = 0
    visited = [False] * (n+1)
    q = [(1, adj[1])]
    longgest = 0
    for curr, next in q:
        for n_v in next:
            if visited[n_v]:
                continue

            if dist[n_v] > dist[curr] + 1:
                dist[n_v] = dist[curr] + 1
                if longgest < dist[n_v]:
                    longgest = dist[n_v]
                    answer = 1
                elif longgest == dist[n_v]:
                    answer += 1
                q.append((n_v, adj[n_v]))

        visited[curr] = True

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))