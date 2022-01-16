n = int(input())
lst = list(map(int,input().split()))
pos = 0
for i in range(0,n-1):
    if lst[i] < lst[i+1] and i != n-1:
        pos = i+1
    else:
        pos = i
        break
print(lst[pos])