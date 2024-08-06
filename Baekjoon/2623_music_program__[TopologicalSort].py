import sys


def topological_sort(a:list, ind:list):
    ans = []
    queue = []

    # 진입 차수가 0인 것만 queue 에 저장
    for i in range(1, len(ind)):
        if ind[i] == 0:
            queue.append(i)

    while queue:
        ans.append(queue.pop(0)) # 진입 차수가 0인 node 만 저장
        for next in a[ans[-1]]:
            ind[next] -= 1

            if ind[next] == 0:
                queue.append(next)

    return ans

def solution():
    singers, pds = map(int, sys.stdin.readline().split())

    arr = [[] for _ in range(singers + 1)]
    indeed = [0 for _ in range(singers + 1)]

    # 위상 정렬 생성
    for _ in range(pds):
        order = tuple(map(int, sys.stdin.readline().split()))
        for i in range(1, order[0]):
            arr[order[i]].append(order[i+1])
            indeed[order[i+1]] += 1

    ans = topological_sort(arr, indeed)
    if len(ans) == singers:
        print('\n'.join(map(str, ans)))
    else:
        print(0)
        
solution()