def bubble_sort(input_list):
    sorted = False
    length = len(input_list) - 1

    while not sorted:
        sorted = True #assume it is sorted
        for i in range(length):
            if input_list[i] > input_list[i+1]:
                sorted = False # find a position not sorted
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]

    return input_list

if __name__ == '__main__':
    my_list = [12, 5, 13, 8, 9, 65]
    print(bubble_sort(my_list))