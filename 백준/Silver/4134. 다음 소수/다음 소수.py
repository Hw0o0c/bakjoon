t = int(input())

for i in range(t):
    n = int(input())
    if n <= 1:
        print(2)
        continue
    start = n    
    
    while True:
        j = 2
        b = 0
        
        while(j < int(start**(1/2))+1):
            if start % j == 0:
                b = 1
                break
            else:
                j += 1
                
        if b == 0:
            print(start)
            break
        else:
            start += 1
        