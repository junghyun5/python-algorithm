#BackJoon Algorithm NO.4779
#Recursion

def CantorianSet(N):
    set1 = ['-'] * (3**N)
    
    

while True:
    try:
        N = int(input())
        CantorianSet(N)
    except : # EOF 
        break