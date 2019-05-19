def binary_search_rotated(arr, key):
    #TODO: Write - Your - Code
    l, r = 0, len(arr) - 1

    if l > r:
        return -1
    while l <= r:
        mid = l + (r-l)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] >= arr[l] and arr[l] <= key <= arr[mid]:
            r = mid - 1
        elif arr[mid] <= arr[r] and arr[mid] <= key <= arr[r]:
            l = mid + 1
        elif arr[mid] <= arr[l]:
            r = mid - 1
        elif arr[mid] >= arr[r]:
            l = mid + 1

    return -1


position = binary_search_rotated([6, 7, 8, 9, 1, 2, 3, 4, 5], 4)
print(position)