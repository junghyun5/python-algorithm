#BackJoon Algorithm NO.1735
#Number theory
import sys
input = sys.stdin.readline

a,b =  map(int,input().split())
c,d =  map(int,input().split())

num = a*d + c*b
den = b*d
def gcd(x,y):
    while y != 0:
        x,y = y, x % y
    return x
        
n = gcd(num,den)

print(num//n, den//n)