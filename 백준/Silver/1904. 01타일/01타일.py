def m_mult(A,B):#n행렬과 m행렬의 곱
    temp = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += A[i][k] * B[k][j]
    return temp
                                                                                                                                                                
def m_pow(n, m):#m행렬을 n만큼 제곱
    if (n== 1):
        return m
    if (n % 2 == 0):
        temp = m_pow(n//2, m)
        return m_mult(temp, temp)
    else:
        temp = m_pow(n-1, m)
        return m_mult(temp, m)

n=int(input())
f=[[1,1],[1,0]]
oup = m_pow(n,f)
print((oup[0][0])%15746)