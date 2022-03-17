"""
At a high level, mergesort applies the three steps of divide and conquer to sort a list of numbers:

1) Divide: Split the list into two (approximately) equally sized lists.

2) Conquer: Sort each of the two lists separately (using mergesort itself!).

3) Combine: Given two sorted lists of approximately the same size, merge them into one big sorted list.


We can also describe the steps of the algorithm a little differently:

Split the NN elements of the list into NN separate lists, each of size one.
Pair adjacent lists and merge them, resulting in about half as many lists each about twice the size.
Repeat step 2 until you have one list of size N.
"""


def merge_two_sorted(list1, list2):
    size_1 = len(list1)
    size_2 = len(list2)

    i, j = 0, 0

    output = []
    while i < size_1 and j < size_2:
        if list1[i] < list2[j]:
            output.append(list1[i])
            i += 1
        else:
            output.append(list2[j])
            j += 1

    return output + list1[i:] + list2[j:]


def sort_recursively(arr):
    if len(arr) == 1:
        return arr
    # First, find middle point
    middle_index = len(arr) // 2

    # Divide into Left and Right arrays
    L = arr[:middle_index]
    R = arr[middle_index:]

    # Reassign the sorted L and R
    L = sort_recursively(L)
    R = sort_recursively(R)

    return merge_two_sorted(L, R)


print(sort_recursively([3.8, -2, 1, 6, 5, 1]))
