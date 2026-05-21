from typing import List
from sys import maxsize


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, temp, i, j, ai, aj, n = -maxsize-1, 0, 0, 0, 0, 0, len(nums)
        for k in range(n):
            temp += nums[k]
            if temp >= ans:
                j = k
                if temp > ans:
                    ai, aj = i, j
                    ans = temp
                else:
                    if j-i > aj-ai:
                        ai, aj = i, j
            if temp < 0:
                temp = 0
                i = k
        print(nums[ai:aj+1])
        return ans
    
nums = [-2,1,-3,4,-1,2,1,-5,4]

# Create object
obj = Solution()

# Call function
result = obj.maxSubArray(nums)

print("Maximum Sum:", result)    