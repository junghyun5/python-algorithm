#BackJoon Algorithm NO.2447
#Recursion

# wrong idea 
# def blank(N):
#     arr1 = []
#     for _ in range(N):
#             row = " " * N
#             arr1.append(row)
#     return arr1
        
def drwStar(N):
    if N == 1:
        return ["*"]
    
    mid = drwStar(N//3)
    arr = []
    
    for i in range (3):
        for j in range(3):
            if i == 1 and j == 1:
                arr.extend([' '* (N//3)]*(N//3))
            else:
                arr.extend(mid)
        
    # wrong idea 02    
    # arr.append("\n")
    # # Use extend instead of append to add each element of mid directly to arr
    
    # arr.extend(mid)
    # arr.extend(blank(N//3))
    # arr.extend(mid)
    # arr.append("\n")
    
    # for _ in range (3):
    #     arr.extend(mid)
        
    return arr

def main():
    N = int(input())
    star = drwStar(N)
    # Join all the elements of the 'star' list into one string, inserting a newline between each element.
    for i in range (N):
        print(star[i], end='')
    
if __name__ == '__main__':
    main()
