#BackJoon Algorithm NO.1037
#Number Theory
import sys
input = sys.stdin.readline 

N = int(input())
M = input()
arr = M.split() #data type : string
arr = list(map(int,arr))
#arr = list(map(int,input().split()))

if (N == 1):
    print(int(M)*int(M))
else:
    print(min(arr)*max(arr))
#No need for loop
#max_n = max(arr)
#min_n = min(arr)
#print(max_n * min_n)