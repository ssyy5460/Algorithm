N = int(input())
lst_tree = list(map(int,input().split()))
lst_tree.sort(reverse = True)

result = []

for i in range(N):
    result.append(lst_tree[i] + i + 1)
print(max(result)+1)