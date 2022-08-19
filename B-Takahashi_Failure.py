n,k = input().split()
n,k = int(n),int(k)

A = list(map(int,input().split()))
B = list(map(int,input().split()))

mx = 0
for i in range(n):
    if A[i] > mx:
        mx = A[i]

check = False

for i in range(n):
    if A[i]==mx and i+1 in B:
        check = True
        break

if check:
    print("Yes")
else:
    print("No")