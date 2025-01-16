#BackJoon Algorithm NO.26069
#Data Structure
import sys
input = sys.stdin.readline

N = int(input())
danc = {'ChongChong'}

for i in range(1, N+1):
    a, b = input().rstrip().split()
    #rstrip() remove all combination of trailing whitespace 
    #or specified characters
    
    if a in danc:
        danc.add(b)
        
    if b in danc:
        danc.add(a)

print(len(danc))
    