n = int(input())
sl,tl = [],[]
for i in range(n):
    s,t = input().split()
    sl.append(s)
    tl.append(t)
# print(sl,tl)
cnt = 0
for i in range(n):
    nickname = False
    for name in [sl[i],tl[i]]:
        check = True
        for j in range(n):
            if i!=j:
                if name == sl[j] or name == tl[j]:
                    check = False
        if check==True:
            nickname = True
    if nickname == True:
        cnt += 1
if cnt>=n:
    print("Yes")
else:
    print("No")