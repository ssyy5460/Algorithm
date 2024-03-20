n = int(input())

# n이 1이거나 2일 경우를 대비한 처리
if n == 1 or n == 2 :
    print(1)
else:
    # 리스트 생성
    arr = [0] * (n+1)

    # 초깃값 설정
    arr[1] = 1
    arr[2] = 1

    # 피보나치 값 넣어주기
    for i in range(3, n+1):
        arr[i] = arr[i-1] + arr[i-2]

    print(arr[n])
