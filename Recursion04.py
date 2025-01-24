#BackJoon Algorithm NO.24060
#Recursion

count = []
# This list will track the order of elements while sorting.

# Merge function to combine two sorted arrays into one sorted array
def merge(arr1, arr2):
    global count
    sorted_a = []
    l,h = 0,0
    while l<len(arr1) and h < len(arr2) :
        if arr1[l] <= arr2[h]:
            sorted_a.append(arr1[l])
            count.append(arr1[l])
            l += 1
        else:
            sorted_a.append(arr2[h])
            count.append(arr2[h])
            h += 1
    
    while l < len(arr1):
        sorted_a.append(arr1[l])
        count.append(arr1[l])
        l += 1
        
    while h < len(arr2):
        sorted_a.append(arr2[h])
        count.append(arr2[h])
        h += 1
        
    return sorted_a

# Merge Sort function that splits the array and recursively sorts it   
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = (len(arr)+1)// 2
    arr1 = merge_sort(arr[:mid])
    arr2 = merge_sort(arr[mid:])
    return merge(arr1, arr2)
    
    
    
def main():
    N, k = map(int,input().split()) # Read N (size of array) and k (k-th element to find
    # for _ in range(N):
    #     num = int(input())
    #     arr.append(num)
    arr = list(map(int,input().split()))
    merge_sort(arr) 
    if len(count) < k: # If there are fewer than k elements in the count list
        print(-1)
    else:
        print(count[k-1]) # Print the k-th element from the count list

if __name__ == '__main__':
    main()

    