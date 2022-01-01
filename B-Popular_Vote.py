from math import *
n,m = map(int,input().split())
l = list(map(int,input().split()))

sum = 0
for i in l:
    sum += i

val = ceil(sum/(4*m))
l.sort(reverse=True)
# print(l)
cnt,ans = 0,False
for i in l:
    if i >= val:
        cnt += 1
        if cnt >= m:
            break
if cnt >= m:
    print("Yes")
else:
    print("No")