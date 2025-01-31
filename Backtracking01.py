#BackJoon Algorithm NO.15649
#Backtracking 

#Using the DFS
def DFS():
    if len(arr) == M: #make a line until M
        print(' '.join(map(str,arr)))
        return
    #Pay attention to the order 
    for i in range(0,N):
        if visited[i] == True: #prevent the same number
            continue
        visited[i] = True #change to the True
        arr.append(i+1) #Put the number in the array
        DFS() #find the next digit
        #Don't put the DFS(arr), it doesn't need it. 
        arr.pop() #start a new line, next i.
        visited[i] = False #reset
        
        

N,M = map(int,input().split())
arr = []
visited = [False] * N
DFS()



