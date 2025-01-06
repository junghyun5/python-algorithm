#BackJoon Algorithm NO.12789
#Stack
import sys
input = sys.stdin.readline

N = int(input())

R = list(map(int,input().split()))
li = []
a = 1

for stu in R:
    li.append(stu) 
    while li and li[-1] == a:
        li.pop()
        a += 1 
        

if li:
    print('Sad')
else:
    print('Nice')    