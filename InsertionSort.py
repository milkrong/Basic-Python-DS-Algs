def insertion_sort(arr_list):
    for i in range(1, len(arr_list)):
        cur = arr_list[i]
        position = i
        while position > 0 and arr_list[position - 1] > cur:
            arr_list[position] = arr_list[position -1]
            position -= 1
        arr_list[position] = cur

    return my_list

my_list = [8,2,1,3,5,4]

print(insertion_sort(my_list))