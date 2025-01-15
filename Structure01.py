#BackJoon Algorithm NO.25192
#Data Structure
import sys
input = sys.stdin.readline

N = int(input())
arr1 = set()
#Use set instead of list for faster lookups 
#Hash Table
cunt = 0 

for i in range(N):
    word = input().strip() #Removes leading
    if word == 'ENTER':#If input the 'ENTER'
        arr1.clear() #Initialize the set
        continue
    elif word in arr1:
        ##If the word aleady exists in the set, do not add it
        continue
    else:
        arr1.add(word)
        #If not, add it to the set
        cunt += 1 
        
print(cunt)
    