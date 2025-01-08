#BackJoon Algorithm NO.1010
#Combinatorics/binomial coefficient
import sys
input = sys.stdin.readline

def factorial(N):
    if N == 0: 
        return 1
    return factorial(N-1) * N

def main():
    T = int(input()) #Iteration count
    for _ in range(T):
        N,M = map(int,input().split()) #West site, East site
        result = factorial(M) // (factorial(N)*factorial(M-N))
        print(result)
        
if __name__ == '__main__':
    main()