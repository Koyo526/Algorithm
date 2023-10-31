#動的計画法
N = 5
length = 10
T = [4,7,5,8,1]
dp = [[False for _ in range(length+1)] for _ in range(N+1)]
dp[0][0] = True

for i in range(N):
    for j in range(length):
        if dp[i][j]:
            dp[i+1][j] = True
            if j + T[i] <= length:
                dp[i+1][j + T[i]] = True

for n in range(N+1):
    print(dp[n])
print("===========================")