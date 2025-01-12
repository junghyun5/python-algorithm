#BackJoon Algorithm NO.10814
#Stable Sorting

n = int(input())
li = []
for i in range(n):
    a,b = input().split()
    a = int(a)
    li.append((a,b))
    
li.sort(key = lambda x: x[0]) # Until the third time
for i in li:
    print(i[0],i[1])