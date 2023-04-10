dp=[[[0 for i in range(21)] for j in range(21)] for k in range(21)]# 3차원 배열을 [21][21][21] 크기로 초기화
def w(a,b,c):
    if (a <= 0 or b <= 0 or c <= 0):#-50부터 0까지
        return 1
    elif(a>20 or b>20 or c>20):
        return w(20,20,20)
    elif (dp[a][b][c] != 0):
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]

a,b,c = map(int, input().split())

while(a != -1 or b != -1 or c != -1):
    print("w({}, {}, {}) = {}".format(a, b, c, w(a,b,c)))
    a,b,c = map(int, input().split())

