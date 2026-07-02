# Returns the leftmost position where the element can be inserted
import bisect
arr = [1, 2, 2, 2, 4, 5]
index = bisect.bisect_left(arr, 2)
print(index)

# Returns the position after the last occurrence.
# index = bisect.bisect_right(arr, 2)
# print(index)

# Inserts an element while keeping the list sorted.
# import bisect
# arr = [1,3,5,7]
# bisect.insort_left(arr,4)
# print(arr)