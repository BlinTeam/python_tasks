import operator

from binary_search import binary_search, binary_search_recursive
from sorts.bubble_sort import bubble_sort
from sorts.quick_sort import quick_sort
from sorts.insertion_sort import insertion_sort
from sorts.merge_sort import merge_sort
from sorts.shell_sort import shell_sort
from sorts.selection_sort import selection_sort

if __name__ == '__main__':
    numbers_list = [1, 4, 5, 9, 10, 10, 10, 15] #[12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 10
    print(binary_search(numbers_list, number_to_find))
    print(binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list)))

    elements = [3, 6, 1, 9, 34, 13]
    bubble_sort(elements)
    elements = [3, 6, 1, 9, 34, 13]
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)
    elements = [3, 6, 1, 9, 34, 13]
    insertion_sort(elements)
    print(elements)
    elements = [3, 6, 1, 9, 34, 13]
    merge_sort(elements)
    print(elements)
    elements = [3, 6, 1, 9, 34, 13]
    shell_sort(elements)
    print(elements)
    elements = [3, 6, 1, 9, 34, 13]
    selection_sort(elements)
    print(elements)

    d = { 'Moscow': 1000000,
          'Saint-Petersburg': 500000,
          'Orsk': 22000,
          'Magnitogorsk': 60000,
          'Murom': 5000,
          'Ekaterinburg': 100000}

    print(d)

    sorted_tuples = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    sorted_dict = {k: v for k, v in sorted_tuples}
    print(sorted_dict)



