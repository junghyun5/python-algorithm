#BackJoon Algorithm NO.24416
#Dynamic programming

n = int(input())

f1, f2 = 0, 0 #number of repetitions. 
def fib(n): #recursive function
    global f1 
    
    if n == 1 or n == 2:
        f1 += 1 #counting
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
f = [0] * (n+1)
def fibonacci(n): #dynamic programming
    f[1] = 1
    f[2] = 1
    global f2 #counting
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        f2 += 1
    return f[n]

fib(n)
fibonacci(n)

print(f1,f2) #compare