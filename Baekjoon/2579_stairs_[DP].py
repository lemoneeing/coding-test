import sys

# 마지막(stairs[N-1])에서부터 시작 
# 탐색 시작 위치 s 로부터 앞 두개를 비교
# selected = N-2 if stairs[N-2] > stairs[N-3]) else N - 3
# if abs(N-1 - selected) > 1:
#   탐색 시작 위치를 selected - 1 로 갱신 -> s 보다 앞 2개를 비교
# else:
#   selected = 무조건 s-3 으로 갱신

def solution():
    N = int(sys.stdin.readline())
    stairs = [int(sys.stdin.readline()) for _ in range(N)]
    values = [[] for _ in stairs]
    
    values[0] = (stairs[0], 0)
    
    if N > 1:
        values[1] = (values[0][0]+stairs[1], stairs[1])
        
        for i in range(2, N):
            values[i] = (values[i-1][1]+stairs[i], max(values[i-2])+stairs[i])
        
    sys.stdout.write(f"{max(values[N-1])}")

solution()