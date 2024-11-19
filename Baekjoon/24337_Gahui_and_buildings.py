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
    if lgR:
        longerPart.extend([l for l in range(longer, 0, -1)])
        ###### longerPart 의 0 번째 값보다 작으면서 shorter 만큼의 숫자 배치
        for s in range(1, longerPart[0]):
            if len(shorterPart) == shorter-1:
                ans = [1] * (N - len(longerPart) - len(shorterPart))
                ans = ans + longerPart[0] + ([1] * (N - longer + 1)) + longerPart[1:]
                break
            
        #     shorterPart.append(s)
            
        # shorterPart.extend([s for s in range(1, shorter)])
        
        # ans = [s for s in range(1, shorter+1)] + longerPart[:1] 
        # ans = ans + ([1] * (N - longer - shorter - len(ans))) + longerPart[1:] + shorterPart[:]
        
        print(longerPart)
        print(shorterPart)
        print(' '.join(list(map(str, ans))))
    else:
        longerPart.extend([l for l in range(1, longer+1)])
        shorterPart.extend([s for s in range(shorter-1, 0, -1)])
        ans = longerPart + shorterPart
        
        print(longerPart)
        print(shorterPart)
        print(' '.join(list(map(str, [1] * (N - len(ans)) + ans))))

solution()