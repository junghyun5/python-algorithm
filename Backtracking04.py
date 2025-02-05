#BackJoon Algorithm NO.15652
#Backtracking 

# A sequence A of length K is said to be non-decreasing if A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK.
def DFS(start):
    if len(arr) == M:
        print(' '.join(map(str,arr)))
        return
    for i in range(start,N): #Same number possible
        arr.append(i+1)
        DFS(i) #include the last number
        arr.pop()


N,M = map(int,input().split())
arr = []
DFS(0)