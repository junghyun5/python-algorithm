#BackJoon Algorithm NO.4949
#Stack
import sys
input = sys.stdin.readline

while True: #Specify the command number
    
    ST = []
    a = input().rstrip()
    
    if a == ".":
        break 

    for j in a:
        
        if j == '(': 
            ST.append(j)
        elif j == ')':
            if ST and ST[-1] == '(': #Last
                ST.pop()
            else:
                print("no")      
                break
        elif j == '[':
            ST.append(j)
        elif j == ']':
            if ST and ST[-1] == '[':
                ST.pop()
            else:
                print("no")
                break
        
    else:
     #Check if there is anything left in the stack 
        if not ST:
            print("yes")
                        
        else:
            print("no")