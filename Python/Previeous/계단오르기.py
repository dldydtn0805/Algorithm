import sys
# sys.stdin = open('input.txt')

n = int(input())
arr= [0]*(n+1)
for i in range(1,n+1):
    arr[i] = int(input())

dp= [0]*(n+1)
dp[1] = arr[1]
if n > 1:
    dp[2] = dp[1] + arr[2]
    for i in range(3,n+1):
        dp[i] = max((dp[i-3]+arr[i-1]+arr[i]), (dp[i-2]+arr[i]))

print(dp[-1])