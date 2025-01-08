#BackJoon Algorithm NO.11050
#Combinatorics/binomial coefficient
def factorial(N):
    if N == 0: #Base 
        return 1
    return factorial(N-1) * N #Recursive

def main():#input range N:1~10, K:0~N
    N,K= map(int,input().split())
    result = factorial(N)//(factorial(K)*factorial(N-K)) #Used integer division
    print(result)
    
    
if __name__ == '__main__':
    main()