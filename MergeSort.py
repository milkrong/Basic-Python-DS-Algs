def merge_sort(arr_list):
    if len(arr_list) == 1:
        return arr_list
    mid = len(arr_list) // 2
    left, right = arr_list[:mid], arr_list[mid:]

    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    result = []
    i_l, i_r = 0, 0
    while i_l < len(left) and i_r < len(right):
        if left[i_l] < right[i_r]:
            result.append(left[i_l])
            i_l += 1
        else:
            result.append(right[i_r])
            i_r += 1

    return result + left[i_l:] + right[i_r:]

my_list = [8,2,1,3,5,4]

print(merge_sort(my_list))
