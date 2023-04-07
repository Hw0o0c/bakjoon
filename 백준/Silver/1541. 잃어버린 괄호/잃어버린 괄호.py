n=str(input())
minus=n.split("-")
for i in range(0,len(minus)):
    if '+' in minus[i]:
        ans=0
        j=minus[i].split("+")
        for k in j:
            ans+=int(k)
        minus[i]=ans

ans=int(minus[0])
for i in range(1,len(minus)):
    ans-=int(minus[i])

print(ans)

    