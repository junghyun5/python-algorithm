#BackJoon Algorithm NO.20920
#Data Structure
import sys
from collections import Counter
input = sys.stdin.readline

N,M = map(int,input().split())
arr = []
voca= []

    
for _ in range (N):
    word = input().rstrip()
    if len(word) >= M:
        arr.append(word)
    
arr1 = Counter(arr).most_common()
arr1_sorted = sorted(arr1, key = lambda x : (-x[1], -len(x[0]), x[0]))

for k, v in arr1_sorted:
    voca.append(k)

for word in voca:
    print(word)