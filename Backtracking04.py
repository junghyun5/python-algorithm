#BackJoon Algorithm NO.15652
#Backtracking 

def DFS(start):
    if len(arr) == M:
        print(' '.join(map(str,arr)))
        return
    for i in range(N): #Same number possible
        arr.append(i+1)
        DFS(i)  
        arr.pop()


N,M = map(int,input().split())
arr = []
DFS(0)