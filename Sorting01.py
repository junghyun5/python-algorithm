#BackJoon Algorithm NO.2750
#Sorting Algorithm/Bubble sort
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
#arr2 = sorted(arr)
for i in range(N-1):
    for j in range(N-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

for ar in arr:
    print(ar)
    
    
