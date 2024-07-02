def solution(sticker):
    answer = 0
    dp = dict(sticker)
    def dynamic_programming(idx, picked ):
        nonlocal dp

        if picked[idx-1]:
        dp[sticker[idx]] = max(dp[sticker[idx-2]] + sticker[idx], dp[sticker[idx-3] + sticker[idx]])
        pass

    return answer

solution([14, 6, 5, 11, 3, 9, 2, 10])