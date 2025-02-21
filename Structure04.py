#BackJoon Algorithm NO.10815
#Structure 

import sys
input = sys.stdin.readline

n = int(input())
arr = set(map(int,input().split()))
N = int(input())
arr2 = list(map(int,input().split()))

for i in range(N):
    if arr2[i] in arr:
        arr2[i] = 1
    else:
        arr2[i] = 0

print(' '.join(map(str,arr2)))