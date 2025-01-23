#BackJoon Algorithm NO.4134
#Number theory

import sys
import math
input = sys.stdin.readline

def sos(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x%i == 0:
            return False
    return True
    
N = int(input())
for i in range(N):
    n = int(input())
    while True:
        if n==0 or n == 1:
            print(2) # 0 and 1 are excluded in advance.
            break
        elif sos(n):
            print(n)
            break
        else:
            n += 1