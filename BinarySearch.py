def binary_search(input_list, item):
    first_index = 0
    last_index = len(input_list) - 1

    while first_index <= last_index:
        mid_index = (first_index + last_index) // 2
        if input_list[mid_index] < item:
            last_index = mid_index - 1
        elif input_list[mid_index] > item:
            first_index = mid_index + 1
        else:
            return mid_index + 1

    return -1


if __name__ == '__main__':
    input = [x for x in range(10)]
    print(binary_search(input,4))

