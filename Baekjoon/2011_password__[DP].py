import sys
input = sys.stdin.readline

def solve():
    pw = input().strip()

    if int(pw[0]) == 0:
        print(0)
        return

    pw_len = len(pw)
    dp = [0] * (pw_len + 1)
    dp[0] = 1   # pw의 2번 자리가 두 자리 수로 해석될 경우를 위한 준비 값. 두 자리 정수로 해석되는 수들은 자신보다 2칸 앞선 암호의 가짓수를 승계
    dp[1] = 1   # pw의 1번 자리의 해석은 무조건 한 가지

    for i in range(2, pw_len+1):
        if int(pw[i-1]) > 0:
            dp[i] += dp[i-1]
                   
        if 10 <= int(pw[i-2:i]) <= 26:
            dp[i] += dp[i-2]
        
        dp[i] %= 1000000
    
    print(dp[pw_len])

solve()