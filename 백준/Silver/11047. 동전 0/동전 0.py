# 동전의 종류와 구하고자 하는 동전의 합
n,k = map(int,input().split())

# 동전 리스트 
coins = []

for i in range(n):
    coins.append(int(input()))
    
# 역순으로 정렬
coins.sort(reverse = True)

cnt = 0

if k == 0:
    print(cnt)
else:
    for c in coins:
        cnt += k // c
        k %= c
    print(cnt)
        