#BackJoon Algorithm NO.11729
#Recursion

def Hanoi(N , start, end):
    if N == 1:
        print(start,end)
        return
    
    Hanoi(N-1, start, 6-start-end) #N-1
    print(start, end) #1
    Hanoi(N-1, 6-start-end, end) #N-1
    

def main():
    N = int(input()) #f(x) = 2^N -1
    print(2**N-1) # 2f(N-1)+1
    Hanoi(N,1,3)
    
if __name__ == '__main__':
    main()