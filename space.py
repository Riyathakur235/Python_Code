# n=5
# for i in range(n):
#     for j in range(2*n-1):
#         if(i==0 or i==n-1 or j==0 or j==2*n-2 or
#             i+j==n-1 or i-j==n-1 + n):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")    
#     print()    
    
# star shape pattern
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i) + "* " * i)
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "* " * i)


# nums = [1,2,3,4,5]
# for num in nums:
#     if num == 3:
#         break
#     else:
#         print("Loop completed")


# merging Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}               # ** are called dictionary unpacking operrator. It use to unpack the key-value pairs from the dictionaries and create a new dictionary with all the key-value pairs combined.
print(merged) 