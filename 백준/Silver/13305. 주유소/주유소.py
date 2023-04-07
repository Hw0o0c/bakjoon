n=int(input())

kilo = list(map(int, input().split()))
g = list(map(int, input().split()))

t=0
ans=0

ans+= g[0] * kilo[0] 

for i in range(1,n-1):

    if(g[t]<g[i]):
        ans+=g[t]* kilo[i]

    else:
        ans+=g[i] * kilo[i]
        t=i

print(ans)
