#BackJoon Algorithm NO.20920
#Data Structure
import sys
from collections import Counter
input = sys.stdin.readline

#Read the number of words N, and minimum length of word M
N,M = map(int,input().split())
arr = []
voca= []

    
for _ in range (N):
    #Don't forget the rstrip()
    word = input().rstrip()
    if len(word) >= M:
        arr.append(word)
    
arr1 = Counter(arr).most_common()
#Count the frequency of each word again, because of lambda
#Sort by the length of the word, sort dictionary order
arr1_sorted = sorted(arr1, key = lambda x : (-x[1], -len(x[0]), x[0]))

for k, v in arr1_sorted:
    voca.append(k)

for word in voca:
    print(word)