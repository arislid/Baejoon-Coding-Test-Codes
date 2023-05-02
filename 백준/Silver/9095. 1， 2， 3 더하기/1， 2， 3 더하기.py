def one_two_three():
    T = int(input())
    ans = []
    for _ in range(T):
        n = int(input())
        dp = [0] * (n+1)
        for i in range(1, n+1):
            if i == 1:
                dp[i] = 1
            elif i == 2:
                dp[i] = 2
            elif i == 3:
                dp[i] = 4
            else:
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        ans.append(dp[n])
    for idx in ans:
        print(idx)


one_two_three()