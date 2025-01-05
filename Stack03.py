#BackJoon Algorithm NO.9012
#Stack
import sys
input = sys.stdin.readline

N = int(input()) #list

for i in range(N): #Specify the command number
    ST = []
    a = input()
    
    for j in a:
        if j == '(':
            ST.append(j)
        elif j == ')':
            if ST:
                ST.pop()
            else:
                print("NO")      
                break
    else: # Check if there is anything left in the stack 
        if not ST:
            print("YES")
        else:
            print("NO")