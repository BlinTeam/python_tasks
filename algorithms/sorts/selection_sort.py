def selection_sort(elements):
    size = len(elements)
    for i in range(size):
        min_index = i
        for j in range(min_index + 1, size):
            if elements[j] < elements[min_index]:
                min_index = j

        if i != min_index:
            elements[i], elements[min_index] = elements[min_index], elements[i]
