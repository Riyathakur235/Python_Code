class Solution:
    def leaders(self, n, arr):
        maxi, n = -1, len(arr)
        ans = []
        for i in range(n-1, -1, -1):
            if arr[i] >= maxi:
                ans.append(arr[i])
                maxi = arr[i]
        return reversed(arr)
    
obj = Solution()

arr = [16, 17, 4, 3, 5, 2]
result = obj.leaders(len(arr), arr)

print(result)    