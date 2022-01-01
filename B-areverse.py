def rev(s, length, l, r) :
    if (l < 0 or r >= length or l > r) :
        return s
    s = list(s)
    # su = s[l:r]
    while (l < r):
        s[l],s[r] = s[r],s[l]
        l += 1
        r -= 1
    return "".join(s)

if __name__ == "__main__":
  l,r = map(int,input().split())
  s = input()
  print(rev(s, len(s), l-1, r-1))