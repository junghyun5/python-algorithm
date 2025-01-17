#BackJoon Algorithm NO.1934
#Number theory
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    a,b =  map(int,input().split())
    aa,bb = a,b
    
    while bb != 0:
        aa= aa%bb
        aa,bb = bb,aa #Euclidean algorithm
        
    print(a*b//aa)