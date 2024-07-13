import sys

def solution(n):
    # N = int(sys.stdin.readline().strip())
    N = n
#     dp = [0 for _ in range(N+1)]
    
#     # 가로 길이가 짝수일 때만 채울 수 있다. (1 <= N <= 30)
#     if N > 1 and N % 2 == 0:
#         dp[2] = 3 
#         dp[i] += dp[i-2] * 3
#         # 가로 길이 4 이상 일 때
#         if N >= 4:
#             dp[4] = 11 # 길이 2일 때 경우의 수(3) * 2칸짜리 가짓 수(3) + 특이 블럭 2개
            
#             for i in range(6, N+1):
#                 # 가로 N 보다 2 짧을 때의 경우의 수 * 2칸짜리 가짓 수 + 이전 경우에서 특이 블럭 * 2 * 2 + 지금 길이에서의 특이 블럭
#                 dp[i] = ((dp[i-2] - 2) * dp[2]) + (2 * 2 * dp[2]) + 2
        

    dp = [0] * 31
    dp[2] = 3
    
    #  가로 길이가 짝수일 때만 채울 수 있다. (1 <= N <= 30)
    if N > 2 and N % 2 == 0:
        
        for i in range(4, N+1):
            # 목표 길이보다 2 짧은 경우 * 길이 2짜리 타일(3가지)
            dp[i] = dp[i-2] * 3
            
            # 이전 길이에서의 특이 블럭(2칸씩 쪼갤 수 없는 타일 구성, 최소 길이 4) 들을 포함하여 채우는 경우
            for j in range(i-4, 0, -2):
                dp[i] += dp[j] * 2
                
            # 목표길이에서의 특이블럭은 항상 2개씩 생김.
            dp[i] += 2
    
    
    
    sys.stdout.write(f"{dp[N]}\n")    
    
solution(1)
solution(2)
solution(3)
solution(4)
solution(5)
solution(6)
solution(7)
solution(8)
solution(9)
solution(10)
# solution()