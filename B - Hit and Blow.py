n = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

cnt1,cnt2 = 0,0
for i in range(n):
    if A[i] == B[i]:
        cnt1 += 1
print(cnt1)
for i in range(n):
    for j in range(n):
        if A[i] == B[j] and i != j:
            cnt2 += 1

print(cnt2)


