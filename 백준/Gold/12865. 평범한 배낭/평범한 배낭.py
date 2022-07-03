n,k = map(int,input().split())
d = [[0] * (k+1) for _ in range(n+1)]
array = [[0,0]]

for i in range(n):
    w,v = map(int,input().split())
    array.append([w,v])
    
for i in range(1,n+1):
    w = array[i][0] # 무게
    v = array[i][1] # 가치
    for j in range(1,k+1):

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j],d[i-1][j-w] + v)
            
print(d[n][k])