s = input()

check_u = False
check_l = False
check_d = False

for i in s:
    if i.islower():
        check_l = True
    else:
        check_u = True

st = set(s)
if len(st) == len(s):
    check_d = True

if check_u and check_l and check_d:
    print("Yes")
else:
    print("No")