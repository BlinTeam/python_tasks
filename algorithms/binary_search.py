def linear_search(numbers_list, numbers_to_find):
    for index, element in enumerate(numbers_list):
        if element == numbers_to_find:
            return index
    return -1


def binary_search(numbers_list, numbers_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == numbers_to_find:
            return mid_index

        if mid_number < numbers_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1
    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        indexes = []
        for i in range(mid_index, len(numbers_list)):
            if numbers_list[i] == mid_number:
                indexes.append(i)
            else:
                break
        return indexes

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)
