n = int(input())

A = []
B = []
for i in range(n):
    x,y = input().split()
    A.append(int(x))
    B.append(int(y))
ans = 1e5
for i in range(n):
    for j in range(n):
        ans = min(ans, A[i]+B[j] if i == j else max(A[i],B[j]))
print(ans)