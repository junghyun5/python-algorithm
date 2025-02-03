#BackJoon Algorithm NO.15650
#Backtracking 

#Using the DFS
def DFS(Num): # (1,3), (3,1) are same. 
    if len(arr) == M: #make a line until M
        print(' '.join(map(str,arr)))
        return 
    for i in range(Num,N):
        if visited[i] == True: 
            continue
        visited[i] = True 
        arr.append(i+1) 
        if arr[0] == N:
            return
        DFS(i+1)  #Add a variable to prevent repetition.
        arr.pop() 
        visited[i] = False 
        
        

N,M = map(int,input().split())
arr = []
visited = [False] * N
DFS(0)