#BackJoon Algorithm NO.9663
#Backtracking 

#divided into two parts.
def queen(i, col):
    global count
    n = len(col) - 1
    if(check(i,col)):
        if(i == n):
            count += 1
        else:
            for j in range(i,n+1):
                col[i+1] = j
                queen(i+1,col)
    
def check(i,col):
    for k in range(i):
        if(col[i] == col[k] or abs(col[i] - col[k]) == (i-k)):
            return False
    return True
    
N = int(input())
count = 0
col = [0] * (N+1)
queen(0,col)
print(count)
