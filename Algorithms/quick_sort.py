"""
Framed in our “divide and conquer” framework:

1) Divide--Pick a pivot element (typically the last item in the array).
All numbers lower than this value go to the left and all elements higher to the right.
For quicksort, this step is commonly known as partitioning.
2) Conquer--All elements to the left are fed recursively back into the algorithm, as are elements to the right.
3) Combine--No need to do anything at all. At this point the data should be sorted.
"""