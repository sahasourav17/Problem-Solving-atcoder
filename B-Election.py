n = int(input())
lst = [input() for i in range(n)]
freq = {}
for nam in lst:
    if nam in freq:
        freq[nam] += 1
    else:
        freq[nam] = 1

s_freq = sorted(freq.items(), key = lambda kv:(kv[1], kv[0]))
s_freq = {k: v for k, v in s_freq}

print(list(s_freq)[-1])

