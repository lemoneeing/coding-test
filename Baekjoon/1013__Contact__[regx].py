import sys
import re

input = sys.stdin.readline

def solve():

    TC = int(input().strip())
    for _ in range(TC):

        in_str = input().strip()
        in_len = len(in_str)

        idx = 0        
        dp = [False] * (in_len + 1)
        dp[idx] = True
        for idx in range(in_len):
            if not dp[idx]:
                continue
                
            # '01' 패턴 확인
            if idx + 1 < in_len and in_str[idx:idx+2] == '01':
                dp[idx+2] = True
            
            # '100+1+' 패턴 확인
            if idx + 2 < in_len and in_str[idx:idx+3] == '100':
                pivot = idx+3

                # 100 이후 0 이 끊길때까지 탐색
                while pivot < in_len and in_str[pivot] == '0':
                    pivot += 1
                
                # 1000... 뒤 1이 하나라도 나오면 True
                while pivot < in_len and in_str[pivot] == '1':
                    dp[pivot+1] = True                    
                    pivot += 1
            
        if dp[in_len]:
            print('YES')
        else:
            print('NO')

solve()