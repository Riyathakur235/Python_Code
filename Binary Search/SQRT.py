class Solution:
    def floorSqrt(self, x):
        if x == 0:
            return 0
        
        low, high, ans = 1, x, -1
        while low <= high:
            mid = (low + high) // 2
            
            if mid * mid <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans
    
x = int(input("Enter number: "))

obj = Solution()
print(obj.floorSqrt(x))    