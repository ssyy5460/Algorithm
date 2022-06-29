num = int(input()) # 숫자입력



for s in range(num):
    sum = 0
    input_str = list(input()) # 괄호 입력
    for s in input_str:
        if s == "(":
            sum += 1
        elif s == ")":
            sum -= 1
        if sum < 0:
            print("NO")
            break
    if sum > 0 :
        print("NO")
    elif sum == 0:
        print("YES")
        