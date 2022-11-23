"""
1) Iterative way
2) Recursive way
"""


# This implementation is wrong. I haven't tested it thoroughly.
def search_iterative(arr, target):
    """
    Works only on sorted arrays.
    :param arr: input array
    :param target: target to search for
    :return: gives the index of the target element if found
    """
    n = len(arr)
    lower_index = 0
    higher_index = n - 1

    mid_index = (lower_index + higher_index) // 2

    while mid_index != lower_index and mid_index != higher_index:
        if target > arr[mid_index]:
            lower_index = mid_index
            mid_index = (lower_index + higher_index) // 2
        elif target < arr[mid_index]:
            higher_index = mid_index
            mid_index = (lower_index + higher_index) // 2
        else:
            return mid_index
    return -1


def search_recursive(arr, target):
    """
    Works only on sorted arrays.
    This is a complicated implementation since I'm using only 2 arguments as opposed to four (arr, target, low, high)
    and the array input here shrinks as you go in recursively. But in those four argument function, array remains same.
    :param arr: input array
    :param target: target to search for
    :return: gives the index of the target element if found
    """
    n = len(arr)
    mid_index = n // 2

    if n == 1:
        # When there's only 1 element, and you'll return based on the value of that one element
        return mid_index if arr[mid_index] == target else -1
    elif target == arr[mid_index]:
        # When more than one elements are there and the target is found at middle value, then directly return
        # middle index.
        return mid_index
    else:
        # This is the case when target is on the right half of the array.
        if target > arr[mid_index]:
            response = search_recursive(arr[mid_index:], target)
            # Needs to add the mid_index whenever the target is found in the right half of the array.
            # And this gets added recursively, so you'll end up with the correct position.
            return mid_index + response if response != -1 else -1
        # This is the case when target is on the left half of the array.
        elif target < arr[mid_index]:
            return search_recursive(arr[: mid_index], target)


print(search_iterative([2, 4, 5, 6, 9, 12, 13, 16], 16))
