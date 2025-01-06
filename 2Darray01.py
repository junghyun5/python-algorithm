#BackJoon Algorithm NO.10798
#2Darray
A = [list(input()) for _ in range(5)]
i_max = max(len(A[i]) for i in range(5))

for i in range(i_max):
  for j in range(5):
    if len(A[j]) > i:
      print(A[j][i], end='')
    else:
      continue