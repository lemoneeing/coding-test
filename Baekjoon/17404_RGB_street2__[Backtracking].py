import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    estmated_cost = []
    for _ in range(N):
        estmated_cost.append(list(map(int, input().split())))

    curr_color = 0  # 중 하나
    min_cost = sys.maxsize
    for order in range(0, N+1):
        curr_color = 0
        painting = [curr_color]  # 실제 색 조합 Queue. 0 과 N-1 번째는 인접으로 침.
        painting_cost = estmated_cost[0][curr_color]
        while curr_color < 3:
            if painting[order-1] != curr_color:
                if order == N and painting[N % order] == curr_color:
                    break
                painting.append(curr_color)
                painting_cost = + estmated_cost[order][curr_color]
            curr_color += 1

        min_cost = min(min_cost, painting_cost)



    '''
    cc[0][0] + cc[1][1] + cc[2][2] ... 조합의 비용을 구해야 함.
    0:0 (o)-> 0:0 + 1:1 -> 0:0 + 1:1 + 2:2
                     -> 0:0 + 1:2 + 2:1 
        (x)-> 0:1 + 1:0 -> 0:1 + 1:0  
        (x)-> 0:2 + 1:0 
    '''

solution()