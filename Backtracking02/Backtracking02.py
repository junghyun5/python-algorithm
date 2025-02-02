#BackJoon Algorithm NO.15650
#Backtracking 

#Using the DFS
def DFS(Num):
    if len(arr) == M: #make a line until M
        print(' '.join(map(str,arr)))
        return
    #Pay attention to the order 
    for i in range(Num,N):
        if visited[i] == True: #prevent the same number
            continue
        visited[i] = True #change to the True
        arr.append(i+1) #Put the number in the array
        DFS(Num+1) #find the next digit
        #Don't put the DFS(arr), it doesn't need it. 
        arr.pop() #start a new line, next i.
        visited[i] = False #reset
        
        #oh

N,M = map(int,input().split())
arr = []
visited = [False] * N
DFS(0)