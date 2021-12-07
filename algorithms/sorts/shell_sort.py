def shell_sort(elements):
    size = len(elements)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = elements[i]
            j = i
            while j >= gap and elements[j - gap] > anchor:
                elements[j] = elements[j - gap]
                j -= gap
            elements[j] = anchor
        gap = gap // 2
