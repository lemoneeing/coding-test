import sys
input = sys.stdin.readline

def solution():
    N, a, b = map(int, input().strip().split())

    if a == N == b:
        sys.stdout.write('-1')

    ans = []
    start = 0
    while len(ans) < N:
        forA = []
        curr = start
        # curr < a 일 동안 ans 에 1 부터 오름차순 추가
        for i in range(a):
            curr += 1
            forA.append(curr)
            if N - len(forA) < b - 1:
                sys.stdout.write('-1')
                return
            
        # 막빌 높이가 b 보다 작으면 b부터 거꾸로 채움.
        if curr > b:
            if N - len(forA) > b:
                ans = forA + [1]*(N-a-b) + [i for i in range(1, b+1)][::-1]
            else:
                print(-1)
                return
            
        # 막빌 높이가 b와 같으면 막빌 -1 부터 거꾸로 b-1까지 채움. b번째부터 1 채움
        elif curr == b:
            ans = forA + [e for e in range(curr-1, 1, -1)]
            if len(ans) < N:
                ans += [ans[-1]-1] * (N - len(ans))

        # 막빌 높이가 b보다 작으면 b - 막빌높이 만큼 더함.
        elif curr < b:
            forA[-1] += b-curr
            ans = forA + [i for i in range(1, b)][::-1]
            
        if len(ans) == N:
            sys.stdout.write(' '.join(list(map(str, ans))))
            return
        
        start += 1

solution()