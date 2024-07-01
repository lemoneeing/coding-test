import sys


n_cnt = int(sys.stdin.readline())
tree = [[]]
visited = [False]
dist = [0]

def BFS(node):
    global visited

    queue = []
    queue.append(node)

    while len(queue) > 0:
        now = queue[0]
        queue.remove(now)
        for peer in tree[now]:
            next = peer[0]
            if not visited[next]:
                queue.append(tree[now][0])
                dist[next] = dist[now] + peer[1]


for n in range(1, n_cnt+1):
    tree.append([])
    visited.append(False)
    dist.append(0)

    n_edges = list(map(int, sys.stdin.readline().split()))
    n_edges.append(-1)
    for adj, w in zip(n_edges[1::2], n_edges[2::2]):
        if adj == -1:
            break

        tree[n].append((adj, w))

visited[1] = True
BFS(1)
max = 1
for n in range(1, n_cnt+1):
    if dist[max] < dist[n]:
        max = n
    visited[n] = False

BFS(max)
dist.sort()
sys.stdout.write(f"{dist[-1]}")