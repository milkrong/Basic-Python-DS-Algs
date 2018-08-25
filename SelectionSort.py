def selection_sort(input_list):
    for i in range(len(input_list)):
        min_idx = i

        for j in range(i+1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j

        input_list[i], input_list[min_idx] = input_list[min_idx], input_list[i]

    return input_list
