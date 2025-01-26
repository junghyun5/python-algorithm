#BackJoon Algorithm NO.2447
#Recursion

def blank(N):
    arr1 = []
    for _ in range(N):
        for _ in range(N):
            arr1.append(" ")
        arr1.append("\n")
        
def drwStar(N):
    arr = []
    if N == 1:
        return ("*")
    mid = drwStar(N//3)
    for _ in range (3):
        arr.append(mid)
    arr.append("/n")
    arr.append (mid)
    arr.append (blank(N//3))
    arr.append(mid)
    arr.append("/n")
    for _ in range (3):
        arr.append(mid)
    return arr

def main():
    N = int(input())
    print("".join(drwStar(N)))
    
if __name__ == '__main__':
    main
