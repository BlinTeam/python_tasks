def merge_two_sorted_lists(a, b, elements):
    i = j = k = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            elements[k] = a[i]
            i += 1
        else:
            elements[k] = b[j]
            j += 1
        k += 1
    while i < len(a):
        elements[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        elements[k] = b[j]
        j += 1
        k += 1


def merge_sort(elements):
    if len(elements) <= 1:
        return

    mid = len(elements) // 2
    left = elements[:mid]
    right = elements[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, elements)
