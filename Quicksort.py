def partition(arr, low, high):
    pivot_value = arr[high]
    pindex = low
    for i in range(pindex, high):
        if arr[i] < pivot_value:
            arr[i], arr[pindex] = arr[pindex], arr[i]
            pindex += 1
    
    arr[pindex], arr[high] = arr[high], arr[pindex]
    print(arr)
    return pindex 

def quick_sort(arr, low, high):
    if low >= high: return 
    pindex = partition(arr, low, high)
    quick_sort(arr, low, pindex - 1)
    quick_sort(arr, pindex + 1, high)

def quick_sort_opertion(arr):
    start, end = 0, len(arr) - 1
    quick_sort(arr, start, end)
    return arr

quick_sort_opertion([3,7,8,5,2,1,9,5,4])
