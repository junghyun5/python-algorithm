#BackJoon Algorithm NO.15649
#Backtracking 

#Using the DFS
def DFS(arr):
    if len(arr) > M: #make a line until M
        print(' '.join(map(str,arr)))
        return
    for i in range(1,N):
        if visited[i] == True:
            continue
        visited[i] = True
        arr.append(i)
        

N,M = map(int,input().split())
arr = []
visited = [False] * N




