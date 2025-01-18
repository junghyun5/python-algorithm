#BackJoon Algorithm NO.2108
#Mathematics
import sys
from collections import Counter
input = sys.stdin.readline


def arithmeticMean(arr1):
    print(round(sum(arr1)/len(arr1)))

def median(arr1):
    if len(arr1) % 2 == 0:
        med = (arr1[len(arr1) // 2 -1]+ arr1[len(arr1) //2])//2
    else:
        med= arr1[len(arr1)//2]
    print(med)
        

def mode(arr1):
    #Fisrt way
    #count = [0] *(max(arr1)+1)
    # for i in arr1: #Counting 
    #     count[i] += 1
        
    # M = 0 #How many mode in the array
    # for i in count:
    #     if i == max(count):
    #         M += 1
    
    # if (M == 1): #if there is only one mode
    #     print(count.index(max(count)))
    # elif(M > 1): 
    #     num = count.index(max(count))
    #     print(arr1[arr1.index(num)-1])
    
    #Second way (so slow)
    # arr2 = arr1.copy() #1D array
    # count = []
    # while len(arr2) != 0:
    #     count.clear()
    #     for i, a in enumerate(set(arr2)): #using set
    #         arr2.remove(a)
    #         count.append(a)
    #     if i == 0:
    #         # This checks the last value of 'i' after the for loop finishes
    #         print(a)
    # if len(count) > 1:
    #     print(count[1])
    
    counter = Counter(arr1)  
    max_count = max(counter.values())  # Find the maximum frequency
    modes = [k for k, v in counter.items() if v == max_count]  # Find all elements with the maximum frequency

    if len(modes) > 1:
        modes.sort()
        print(modes[1])  
    else:
        print(modes[0])  
        
def interval(arr1):
    inter = max(arr1) - min(arr1)
    print(inter)

def main():
    N = int(input())
    arr = [] #not use set

    for _ in range(N):
        A = int(input())
        arr.append(A)
    arr1 = sorted(arr)
    arithmeticMean(arr1)
    median(arr1)
    mode(arr1)
    interval(arr1)

if __name__ == '__main__':
    main()