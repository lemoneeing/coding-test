import sys

def main():
    n = int(sys.stdin.readline())

    D = [[0, 0] for _ in range(n+1)]
    D[1] = [0, 1] # 끝자리에 0 을 추가하여 만들 수 있는 수의 개수:0, 끝자리 1 : 1

    for i in range(2, n+1):
        D[i] = [sum(D[i-1]), D[i-1][0]] # 이전 자리수 중 끝이 0인 수 + 1인 수 의 개수 합, 끝자리 1인 수의 개수

    sys.stdout.write(f"{sum(D[n])}")

if __name__ == "__main__":
    main()