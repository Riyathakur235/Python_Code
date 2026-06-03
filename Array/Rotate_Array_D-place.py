from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        # method 1 : due to some reason not working on leetcode
        # nums = nums[::-1]
        # nums[:k] = nums[:k][::-1]
        # nums[k:] = nums[k:][::-1]
        # print(nums)

        # method 2 :
        nums[:] = nums[n - k:] + nums[:n - k]
        
# Input
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

# Create object
obj = Solution()

# Call function
obj.rotate(nums, k)

# Print rotated array
print(nums)        