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
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# merged = {**dict1, **dict2}               # ** are called dictionary unpacking operrator. It use to unpack the key-value pairs from the dictionaries and create a new dictionary with all the key-value pairs combined.
# print(merged) 

# login 
# username = input("Enter your username: ")
# password = input("Enter your password: ")

# if username == "admin@domain.com" and password == "pass1234":
#     print("Login successful!")
# else:
#     print("Invalid username or password.")


# Duplicate characters in a string
# from unittest import result

# def remove_duplicates(input_string):
#     result = ""
#     for char in input_string:
#         if char not in result:
#             result += char
#     return result

# print(remove_duplicates("programming"))


# Merge two dictionaries and sum values for common keys.
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 25, 'd': 35}

result = {}
for key in dict1:
    result[key] = dict1[key]
    
for key in dict2:
    if key in result: 
        result[key] = result[key] +dict2[key]
    else:
        result[key] = dict2[key]
        
print(result)         