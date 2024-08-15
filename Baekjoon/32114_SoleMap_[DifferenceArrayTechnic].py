import sys

def solution():
    N, M = map(int, sys.stdin.readline().split())
    
    # 도로 상황: w[i] 는 i 와 i+1 도시를 연결하는 도로 수
    roads = [-1]
    for degree in map(int, sys.stdin.readline().split()):
        roads.append(degree)

    # 유동 차량 상황을 '차분 배열'로 정리: traffic[i] 는 i ~ i+1 구간을 이동하는 차량의 수 
    # 차분 배열: 각 구간동안 발생하는 변화량이 다양할 때, 변화량의 차이로 계산하여 각 구간의 누적 합을 구하는 방법
    # ex) 도서관에 책이 총 10권, A 가 1일 ~ 5일 까지 3권 대여, B 가 3일 ~ 8일 까지 5권 대여, 6일에 도서관이 새 책 23권 구매
    #     이 때 7일 ~ 9일 동안 도서관 안에 있는 총 책의 권수는? 과 같은 문제를 풀 때 시간 복잡도를 줄 일 수 있다.
    #     lib = [10, 7, 7, 2, 2, 5, 28, 28, 33, 33] <- 최종적으로 구하려는 배열의 형태
    #     구하는 방법: lib = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10] lib[i] 는 i 일에 도서관에 있는 책의 수
    #     lib[1] -= 3, lib[6] += 3
    #     lib[3] -= 5, lib[9] += 5
    #     lib[6] += 23
    #     lib = [10, -3, 0, -5, 0, 0, 26, 0, 5, 0] -> lib[0] 부터 lib[9] 까지 누적 합을 구한다.
    #     lib = [10,  7, 7,  2, 2, 2, 28, 28, 33, 33]
    traffic = [0] * (N + 2)
    for i in range(M):
        u, v, x = map(int, sys.stdin.readline().split())
        traffic[u] += x
        traffic[v] += -1 * x
    
    for i in range(2, N+2):
        traffic[i] += traffic[i-1]
    
    # print(roads)
    # print(traffic)
    
    # 각 구간 별 최소값
    w = []
    for j, road in enumerate(roads):
        
        if j == 0:
            continue
        
        # 도로가 1개이면 모든 차량이 해당 도로만 이용하므로 차량 수의 제곱
        if road == 1:
            w.append(traffic[j] ** 2)
            
        # 도로가 차량 수보다 크면 각 도로마다 차량이 1대씩 달리게 되므로 (1의 제곱 * 차량 수) = 차량 수
        elif road > traffic[j]:
            w.append(traffic[j])
            
        # 도로 수보다 차량 수가 더 많으면 
        else:
            surplus = traffic[j] % road # 각 도로마다 균등하게 배치하고 남은 나머지 차량 수
            car_per_road = traffic[j] // road # 나머지를 제외하고 각 도로마다 균등하게 배치한 차량 수
            
            # ((각 도로마다 균등하게 배치된 차량 수 + 1) x 나머지 차량 수): 나머지만큼 각 도로에 차량이 1씩 더 추가된다.
            # + (차량이 추가배치되지 않은 도로의 차량 수 의 제곱)
            w.append((surplus * (car_per_road + 1)**2) + ((car_per_road ** 2) * (road - surplus)))
    
    for weight in w:
        sys.stdout.write(f"{weight}\n")
solution()