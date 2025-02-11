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
    k = 1
    check1 = True
    while(k<1 and check1):
        if(col[i] == col[k] or abs(col[i] - col[k]) == (i-k)):
            check1 = False
        k += 1
    return check1
    
N = int(input())
col = [0] * (N+1)
queen(0,col)
