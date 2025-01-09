#BackJoon Algorithm NO.11650
#Sorting
N = int(input())
arr = []
for i in range(N):
    a,b = map(int,input().split())
    arr.append((a,b)) #2Darray is stored in the same way.
arr.sort()
for i in range(N):
    print(arr[i][0],arr[i][1])