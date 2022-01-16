from itertools import permutations
s = input()
ans = set()

for i in range(len(s),len(s)+1):
    for c in permutations(s,i):
        ans.add(c)
print(len(ans))