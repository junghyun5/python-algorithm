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
    #Different solution
    # result = 1
    # for i in range(K):
    #     result *= N
    #     N -= 1
    # divs = 1
    # for i in range(2,K+1):
    #     divs *= 1
    #print(result // divs)
    
if __name__ == '__main__':
    main()