n = int(input())

n1, n2 = 0,1

for i in range(n):
    n1, n2 = n2, n1+n2
    
print(n1)