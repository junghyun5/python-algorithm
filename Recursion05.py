#BackJoon Algorithm NO.4779
#Recursion

def CantorianSet(set1):
    
    
    
    

while True:
    try:
        N = int(input())
        set1 = ['-'] * (3**N)
        CantorianSet(set1)
    except : #EOF: Stops execution when writing stops (end of file)
        break