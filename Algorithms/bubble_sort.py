"""
Bubble sort is a simple sorting algorithm. This sorting algorithm is comparison-based algorithm in which each pair of
adjacent elements is compared and the elements are swapped if they are not in order.
This algorithm is not suitable for large data sets as its average and worst case complexity are of Ο(n2)
where n is the number of items.
"""


def sort_iteratively(arr):
    swapped = False
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = True

        if not swapped:
            break

    return arr


print(sort_iteratively([3.8, -2, 1, 6, 5, 3, 1, 5, 6]))
