def two_sum(nums: list[int],target: int) -> list[int]:
    seen = {}
    for index, num in enumerate(nums):
        complement = target -num
        if complement in seen:
            return[seen[complement],index]
        # stroe the current number and its index in the dictionary
        seen[num ] = index      
        
    return[]    #Return empty list if no solution is found