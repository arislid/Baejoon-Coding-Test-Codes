def fibo_01():
    def find_zero_one(n):
        dp = [[0, 0]] * (n + 1)
        for i in range(n+1):
            res = [0, 0]
            if i == 0:
                dp[i] = [1, 0]
            elif i == 1:
                dp[i] = [0, 1]
            else:
                res[0] = dp[i-1][0] + dp[i-2][0]
                res[1] = dp[i-1][1] + dp[i-2][1]
                dp[i] = res
        return dp[n]

    N = int(input())
    ans = []
    for i in range(N):
        n = int(input())
        ans.append(find_zero_one(n))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1])
        
fibo_01()