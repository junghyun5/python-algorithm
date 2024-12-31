#BackJoon Algorithm NO.2566
N = []
A = -1 #min 0 max99
B,C= 0,0
for i in range(9):
    N.append([]) #2D array
    #or N = [list(map(int,input().split())) for _ in range(9)]
    N[i] = list(map(int,input().split()))
    for j in range(9): 
        if N[i][j] > A:
            A = N[i][j]
            B = i + 1
            C = j + 1

print(A)
print(B, C)