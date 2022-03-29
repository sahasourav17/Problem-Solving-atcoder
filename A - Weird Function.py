n = int(input())

def weird(x):
    ans = (x*x) + 2*x + 3
    return ans

print(weird(weird(weird(n)+n)+weird(weird(n))))
