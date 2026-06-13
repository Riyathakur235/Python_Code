from typing import List
import bisect


class Solution:
    def rowWithMax1s(self, arr: List[List[int]], n: int, m: int):
        maxi, index = 0, -1
        for i in range(n):
            count = m - bisect.bisect_left(arr[i], 1)
            if count > maxi:
                maxi, index = count, i
        return index
    
# Input matrix
arr = [
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]
]

n = len(arr)
m = len(arr[0])

# Create object
obj = Solution()

# Call function
result = obj.rowWithMax1s(arr, n, m)

print("Row with maximum 1s:", result)    