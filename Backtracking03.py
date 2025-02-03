#BackJoon Algorithm NO.15651
#Backtracking 

def DFS():
    if len(arr) == M:
        print(' '.join(map(str,arr)))
        return
    for i in range(N): #Same number possible
        arr.append(i+1)
        DFS()  
        arr.pop()


N,M = map(int,input().split())
arr = []
DFS()