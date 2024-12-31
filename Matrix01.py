#BackJoon Algorithm NO.2738
N,M = map(int,input().split) #matrix size
A = [] #make array
B = []
for i in range(N): #input the array 
    A.append([])
    A[i] = list(map(int,input().split()))

for i in range(N):
    B.append([])
    B[i] = list(map(int,input().split()))

for i in range(N): #Matrix Sum
    for j in range(M):
        print(A[i][j]+B[i][j], end=' ')
    print()

