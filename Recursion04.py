#BackJoon Algorithm NO.24060
#Recursion

def merge(arr1, arr2):
    sorted_a = []
    l,h = 0,0
    while l<len(arr1) and h < len(arr2) :
        if arr1[l] <= arr2[h]:
            sorted_a.append(arr1[l])
            l += 1
        else:
            sorted_a.append(arr2[h])
            h += 1
    
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    arr1 = merge_sort(arr[:mid])
    arr2 = merge_sort(arr[mid:])
    merge(arr1, arr2)
    

    