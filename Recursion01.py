#BackJoon Algorithm NO.27433
#Recursion
import sys
input = sys.stdin.readline

def factorial(N):
    if N <= 1:
        return 1
    return factorial(N-1)*N

def main():
    N = int(input())
    Fac = factorial(N)
    print(Fac)

if __name__ == '__main__':
    main()