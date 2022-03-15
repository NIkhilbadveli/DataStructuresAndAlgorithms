"""
***Also known as Bubble sort

1) Designate the leftmost element of AA as the only element of the sorted side.
This side is guaranteed to be sorted by default, since it now contains only one element.
2) Insert the first element of the unsorted side into the correct place in the sorted side,
increasing the number of sorted elements by one.
3) Repeat step two until there are no unsorted elements left.

Worst case time complexity =  O(n^2)
Best case = O(n)

Space complexity is O(n)"""


def sort_iteratively(arr):
    """
    Uses the above algorithm.
    Time complexity = O(n^2) since there are 2 for loops.
    :param arr:
    :return:
    """
    sorted_arr = [arr[0]]
    sorted_arr.insert(0, arr[1]) if arr[1] < sorted_arr[0] else sorted_arr.append(arr[1])
    for i in range(2, len(arr)):
        for j in range(len(sorted_arr)):
            if arr[i] <= sorted_arr[j]:
                sorted_arr.insert(j, arr[i])
                break
            elif sorted_arr[j] < arr[i] < sorted_arr[j + 1]:
                sorted_arr.insert(j + 1, arr[i])
                break
            elif j == len(sorted_arr) - 2:
                sorted_arr.append(arr[i])
                break
    return sorted_arr
