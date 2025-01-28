#BackJoon Algorithm NO.11729
#Recursion

def Hanoi(N , start, end):
    if N == 1:
        print(start,end)
    
    Hanoi(N-1, start, 6 - start -end)
    print(start, end)
    Hanoi(N-1, 6 -start -end, end)
    

    