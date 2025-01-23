#BackJoon Algorithm NO.2485
##Number theory

import sys
import math
input = sys.stdin.readline

def gcd(x,y):
    while y != 0:
        x,y = y,x%y
    return x

n = int(input())
cnt = 0 # 숫자 세기 위한 변수 선언
 
arr = sorted([int(input()) for _ in range(n)])
#list 만들고 정렬. 컴프리헨션 
    
sub = []

for i in range(len(arr) -1):
    sub.append(arr[i+1] - arr[i])
# 가로수들의 차이를 리스트에 저장

gcd1 = sub[0]
for i in range(1,len(sub)):
    gcd1 = gcd(gcd1,sub[i]) #각각의 최대공약수 구하기 

for j in sub:
    cnt +=  j // gcd1 -1 #-1은 왜 해주냐면 그 사이에 심는 거잖아.
    
print(cnt)