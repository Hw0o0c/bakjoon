b=0

arr=[0]*41
arr[1]=1
arr[2]=1

def fibonacci(n):
    global a
    global b
    
    if (n==1 or n==2):
        return 1
    for i in range(3,n+1):
        b+=1
        arr[i]=arr[i-1]+arr[i-2];
    return arr[n]


n=int(input())
fibonacci(n)
print(arr[n], b)

