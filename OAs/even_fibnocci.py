def solution(_max):
    # Type your solution here 
    dp = [0]*_max
    fb = [0]*_max
    if _max == 1:
        return 0
    if _max == 2:
        return 2
    
    fb[0], fb[1] = 1, 2
    dp[0], dp[1] = 0, 2
    i = 2
    while i < _max:
        fb[i] = fb[i-1]+fb[i-2]
        if fb[i] % 2 == 0:
            dp[i] = fb[i] + dp[i-1]
        else:
            dp[i] = dp[i-1]
    
    return dp[i]

print(solution(10))