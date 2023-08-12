n = int(input())

count = 1
m = 3

while(n > 0):
    n -= m
    if n <= 0:
        break
    else:
        count += 1
        m += 2
print(count)
