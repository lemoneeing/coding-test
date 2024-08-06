import sys

def solution():
    n, m = map(int, sys.stdin.readline().split())
    arr_list = [[] for i in range(n+1)]
    indegree = [0] * (n + 1)

    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        arr_list[a].append(b)
        indegree[b] += 1

    # 진입 차수가 0인 것부터 탐색하도록 정렬
    q = []
    for nd, v in enumerate(indegree[1:]):
        if v == 0:  
            q.append(nd+1)

    while q:
        now = q.pop(0)
        sys.stdout.write(f"{now} ")

        for next in arr_list[now]:
            indegree[next] -= 1 # next 로 가는 node 를 뺐으므로 next 의 진입 차수 감소

            if indegree[next] == 0:
                q.append(next)

solution()