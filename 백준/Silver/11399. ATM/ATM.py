n=int(input())
ans=0
p = list(map(int, input().split()))
p.sort()

for i in range(0,n):
    ans += p[n-i-1] * (i+1)
    
print(ans)    


