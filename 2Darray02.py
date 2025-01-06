#BackJoon Algorithm NO.2563
#2Darray
A = [[0]*100 for _ in range(100)]
N = int(input())
for i in range(N):
  a,b = map(int,input().split())
  for x in range (10):
    for y in range (10):
      A[a+x][b+y] = 1

result = 0
for i in range(100):
  result += A[i].count(1)

print(result)