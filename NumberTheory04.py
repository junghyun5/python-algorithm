#BackJoon Algorithm NO.2485
#Number theory

import sys
import math
input = sys.stdin.readline

def gcd(x,y):
    while y != 0:
        x,y = y,x%y
    return x

n = int(input())
cnt = 0 # Declare a variable to count the numbers
 
arr = sorted([int(input()) for _ in range(n)])
#Create a list and sort it using list comprehension
    
sub = []

for i in range(len(arr) -1):
    sub.append(arr[i+1] - arr[i])
#  Store the differences between the trees in a list

gcd1 = sub[0]
for i in range(1,len(sub)):
    gcd1 = gcd(gcd1,sub[i]) #Calculate the greatest common divisor for each of the differences 

for j in sub:
    cnt +=  j // gcd1 -1 #The -1 is because we're planting trees in between the existing ones.
    
print(cnt)