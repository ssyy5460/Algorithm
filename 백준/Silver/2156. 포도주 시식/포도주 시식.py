import sys
read = sys.stdin.readline

N = int(read())
array = [0] + [int(read()) for _ in range(N)] + [0]
d = [0] * (N+2)
d[1] = array[1]
d[2] = array[1] + array[2]

for i in range(3, N+1):
    d[i] = max(d[i-3]+array[i-1]+array[i], d[i-2]+array[i], d[i-1])
print(d[N])