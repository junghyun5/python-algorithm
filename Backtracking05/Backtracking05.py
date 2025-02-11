#BackJoon Algorithm NO.9663
#Backtracking 

#divided into two parts.
def queen(i, col):
    n = len(col) - 1
    # col = [0,0,0, ... ,0]
    #first one is 
    if(check(i,col)):
        if(i == n):
            print(col[1: n+1])
    else:
        for j in range(i,n+1):
            col[i+1] = j
            queen(i+1,col)
    
def check(i,col):
    

N = int(input())
