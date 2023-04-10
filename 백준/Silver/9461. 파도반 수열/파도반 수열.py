dp=[0 for i in range(101)]
dp[1],dp[2],dp[3],dp[4],dp[5]=1,1,1,2,2

def p(n):
    if(n <= 5):
        return dp[n]
    for i in range(5,n+1):
        if(dp[n]!=0):
            return dp[n]
        else:
            dp[n]=p(n-1) + p(n-5)
            return dp[n]

T=int(input())

for i in range(T):
    n=int(input())
    print(p(n))