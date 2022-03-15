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