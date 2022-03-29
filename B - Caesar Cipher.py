s1 = input()
s2 = input()

check = set()
for i,j in zip(s1,s2):
    l = (ord(i) - ord(j) + 26)%26
    check.add(l)

if len(check) == 1 :
    print("Yes")
else:
    print("No")
