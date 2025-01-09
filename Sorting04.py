#BackJoon Algorithm NO.11651
#Sorting
import sys

n = int(input())
li = []

for i in range(n):
    a,b = map(int,sys.stdin.readline().split()) 
    li.append([a,b])
    
li.sort(key=lambda x : (x[1], x[0])) 
#When creating a short function, it is used and prioritized.
for i in li:
    print(i[0],i[1])