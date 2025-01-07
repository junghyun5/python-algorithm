#BackJoon Algorithm NO.10872
#Combinatorics
def factorial(num1): #Solution using a recursive function
    if num1 == 0:
        return 1
    return factorial(num1-1)*num1

def main():
    N = int(input())
    mul = 1
    print(factorial(N))
    # for i in range(1,N+1): #Solution with for loop
    #     if N == 0:
    #         print(1)
    #         break
    #     mul *= i
    # print(mul)
    
if __name__ == "__main__":
    main()