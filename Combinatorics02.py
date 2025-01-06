#BackJoon Algorithm NO.24723
#Combinatorics
#print(2**N) Easy Answer 
def Combinatoric(Num1): #Using recursive function.
    if Num1 <= 1:
        return 2
    return Combinatoric(Num1-1) * 2 #Don't squared.

def main():
    N = int(input())
    print(Combinatoric(N))
    
if __name__ == '__main__':
    main()    