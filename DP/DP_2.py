#動的計画法
N = 5
length = 10
T = [4,7,5,8,1]

money = 500
price = [150, 200, 250,200,50]
money = money // 50
price = list(map(lambda x: x//50 ,price))
print(money,price)
dp = [[-1 for _ in range(length+1)] for _ in range(N+1)]
for i in range(money+1):
    dp[0][i] = 0
for i in range(N):
    for j in range(money+1):
        if price[i] <= j: 
            dp[i+1][j] = max(dp[i][j-price[i]]+T[i],dp[i][j])
        else:
            dp[i+1][j] = dp[i][j]

for n in range(N+1):
    print(dp[n])
print("===========================")