"""
Framed in our “divide and conquer” framework:

1) Divide--Pick a pivot element (typically the last item in the array).
All numbers lower than this value go to the left and all elements higher to the right.
For quicksort, this step is commonly known as partitioning.
2) Conquer--All elements to the left are fed recursively back into the algorithm, as are elements to the right.
3) Combine--No need to do anything at all. At this point the data should be sorted.
"""


def sort_recursively(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    # Divide into Left and Right arrays
    L = []
    R = []
    duplicate_count = 0
    for e in arr:
        if e < pivot:
            L.append(e)
        elif e > pivot:
            R.append(e)
        else:
            duplicate_count += 1

    # Reassign the sorted L and R
    L = sort_recursively(L)
    R = sort_recursively(R)

    return L + [pivot] * duplicate_count + R


print(sort_recursively([3.8, -2, 1, 6, 5, 3, 1, 5, 6]))
