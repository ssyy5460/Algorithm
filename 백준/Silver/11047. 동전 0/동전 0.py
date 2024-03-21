n,k = map(int,input().split()) # 동전의 종류와 동전의 합
coins = []
for i in range(n):
    coins.append(int(input())) # 동전들의 모임
coins.sort(reverse = True) # 가장 큰 동전이 오게 역순으로 정렬

cnt = 0
for val in coins: 
    if k == 0: # 동전의 합이 0이라면..
        break
    else:
        while val <= k: # 동전의 합이 val보다 크거나 같다면
            k -= val 
            cnt += 1
print(cnt)
            