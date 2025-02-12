#BackJoon Algorithm NO.9663
#Backtracking 

#divided into two parts.
def queen(i):
    global count  
    n = len(col)
    if(i == n):
        count += 1
        return
    else:
        for j in range(n):
            col[i] = j
            if check(i):
                queen(i+1)
    
def check(i):
    for k in range(i):
        if(col[i] == col[k] or abs(col[i] - col[k]) == (i-k)):
            return False
    return True
    
N = int(input())
count = 0
col = [0] * (N)
queen(0)
print(count)
