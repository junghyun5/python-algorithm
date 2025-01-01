#BackJoon Algorithm NO.28278
#Stack
import sys
input = sys.stdin.readline

N = int(input())
ST = [] #list

for i in range(N): #Command Numbering
    op = input().split()
    if op[0] == '1':
        ST.append(int(op[-1])) # Put a integer
    elif op[0] == '2': #Take out the last number.
        if ST:
            print(ST.pop(-1))
            continue
        print(-1)
    elif op[0] == '3':
        print(len(ST))
    elif op[0] == '4':
        if ST:
            print(0)
            continue
        print(1)       
    elif op[0] == '5':
        if ST:
            print(ST[-1])
            continue
        print(-1)