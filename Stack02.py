#BackJoon Algorithm NO.10773
#Stack
import sys
input = sys.stdin.readline

N = int(input())
ST = [] #list

for i in range(N): #Specify the command number
    op = input()
    
    if op[0] != '0':
        ST.append(int(op)) # stack
    else:
        ST.pop(-1)
        

print(sum(ST))