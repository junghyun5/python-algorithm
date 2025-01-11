#BackJoon Algorithm NO.1181
#Sorting
import sys
n = int(input())
li = []

# for i in range(n):
#     a = map(str,sys.stdin.readline()) 
#     li.append(a)
# li = list(set(li))
# for i in range(n-1):
#     if len(li[i])>len(li[i+1]):
#         t = li[i]
#         li[i] = li[i+1]
#         li[i+1] = t
#     elif len(li[i]) == len(li[i+1]):
        
# li.sort(key=lambda x : (x[1], x[0])) #sorting
# for i in li:
#     print(i[0],i[1])

for i in range(n):
    li.append(input())

li = list(set(li))
li.sort() #using sort 
li.sort(key = len) #Sort the list based on the length of each string

for i in li:
    print(i)