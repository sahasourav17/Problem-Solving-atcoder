s = input()
ans = ''

for i in range(len(s)):
    if s[i] == '9':
        ans += ''+'6'
    elif s[i] == '6':
        ans += ''+'9'
    else:
        ans += ''+s[i]
print(ans[::-1])
