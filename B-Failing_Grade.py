n,m = map(int,input().split())
l = list(map(int,input().split()))
l = sorted(l)
cnt = 0
for i in l:
    if i >= m:
        break
    else:
        cnt += 1
print(cnt)
