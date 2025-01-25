#BackJoon Algorithm NO.4779
#Recursion
import sys
input = sys.stdin.readline

def CantorianSet(N):
    if N == 1:
        return '-'
    onesd = CantorianSet(N // 3)
    cantorset = onesd + ' ' * len(onesd) + onesd
    return cantorset

while True:
    try:
        N = int(input())
        Numb = 3**N
        print(CantorianSet(Numb))
    except : #EOF: Stops execution when writing stops (end of file)
        break