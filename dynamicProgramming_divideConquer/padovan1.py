n = int(input())

# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9

dp = [0]*(n+1)

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for i in range(6, n+1):
    dp[i] = dp[i-1]+dp[i-5]


print(dp[int(input())])