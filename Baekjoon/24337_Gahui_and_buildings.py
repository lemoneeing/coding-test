import sys
input = sys.stdin.readline

def solution():
    N, a, b = map(int, input().strip().split())
    lgR = False
    if a > b:
        longer = a
        shorter = b
        lgR = False
    else:
        longer = b
        shorter = a
        lgR = True
    
    if N - longer < shorter - 1:
        sys.stdout.write('-1')
        return

    ans = []
    longerPart = []
    shorterPart = []
    
    # 가희친구가 볼 수있는 빌딩이 더 많을 때
    if lgR:
        longerPart.extend([l for l in range(longer, 0, -1)])
        shorterPart.extend([s for s in range(1, shorter)])
        
        if longer + shorter > N:
            ans = shorterPart[:shorter] + longerPart
        
        elif longer + shorter == N:
            shorterPart[-1] = longerPart[0]
            ans = shorterPart + longerPart
        
        else:
            if shorter == 1:
                ans = [longerPart[0]] + ([1] * (N - longer - shorter + 1)) + longerPart[1:]
            else:
                ans = [shorterPart[0]] + ([1] * (N - longer - shorter + 1)) + shorterPart[1:] + longerPart
    else:
        longerPart.extend([l for l in range(1, longer+1)])
        shorterPart.extend([s for s in range(shorter, 0, -1)])
        
        if longer + shorter > N:
            ans = longerPart + shorterPart[1:]
        
        elif longer + shorter == N:
            shorterPart[0] = longerPart[-1]
            ans = longerPart + shorterPart
        
        else:
            ans = ([1] * (N - longer - shorter + 1)) + longerPart + shorterPart[1:]
            
    sys.stdout.write(' '.join(list(map(str, ans))))

solution()