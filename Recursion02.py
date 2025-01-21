#BackJoon Algorithm NO.10870
#Recursion
import sys
input = sys.stdin.readline

def Fibonacci(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return Fibonacci(N-2) + Fibonacci(N-1)
    
def main():
    N = int(input())
    Fi = Fibonacci(N)
    print(Fi)
    
if __name__ == '__main__':
    main()