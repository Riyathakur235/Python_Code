# Walrus Operator
# if(n := len([1,2,3,4,5])) >3:
#     print(f"List is too long ({n} elements, expected <=3)")
    
#Types Definitions in Python
# Variable type
# n : int = 5
# name : str = "Rahul"
# Function Type
# def sum(a: int, b:int) -> int:
#     return a+b

# Match Case
# def http_status(status):
#     match status:
#         case 200:
#             return "OK"
#         case 404:
#             return "Not Found"
#         case 500:
#            return "Internal Server Error"
#         case _:
#            return "unknown status"  
            
# # print(http_status(200))
# # print(http_status(404))
# print(http_status(500))

# Dictionary merge & update
# dict1 ={'a':1,"b":2}
# dict2 ={"b":3 ,"c":4}
# merged = dict1 | dict2
# print(merged)
              
# multiple file open
# with(
#     open('file1.txt') as f1,
#     open('file2.txt') as f2
# ):   


# Exception Handling 
# try:
#     a=int(input("Hey,Enter a number : "))
#     print(a) 
# except Exception as e:
#     print(e)    
# print("Thankyou")
# we can also throw the particular type of error
   
# Raising Exception
# a=int(input("Enter a number: "))
# b=int(input("Enter second number: "))
# if(b==0):
#     raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
# else:
#    print(f"The division a/b is {a/b}")


#   try with else
# try:
#     a=int(input("Hey,Enter a number : "))
#     print(a) 
# except Exception as e:
#     print(e)  
    
# else:
#     print("I am inside else") 

# Try with finally    
# def main():
#  try:
#     a=int(input("Hey,Enter a number : "))
#     print(a) 
#     return
#  except Exception as e:
#     print(e)  
#     return
#  finally:                                finally always run if try and catch return the value
#     print("I am inside finally") 

# main()    


# def myFunc():
#     print()
    
# myFunc()
# print(__name__)  

# global keyword
# a=89
# def fun():
#     global a
#     a=3
#     print(a)
    
# fun()
# print(a)    
      
      
#  Enumerate function
l =[3,45,67,764]
# index=0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index +=1

# THis can be simplified using enumerate function
# for index,item in enumerate(l):
#     print(f"The item number at index {index} is {item}")

# List Comprehension
myList =[1,2,6,7,8,6]
# squaredList =[]
# for item in myList:
#     squaredList.append(item*item)

# This can be simplified using list comprehension
# squaredList = [item*item for item in myList]
# print(squaredList)


# Practice Questions
# try:
#     with open("1.txt") as f:
#         print(f.read())
# except Exception as e:
#     print(e)    
# print("Thankyou") 

# print third ,fifth and seventh elememt of the list using enumerate fun
# l=[1,2,3,4,5,6,7,8]
# for i,item in enumerate(l):
#     if i==2 or i==4 or i==6:
#         print(item)

# write a list comprehension to print a list which contains the multiplication table of a user entered number.
# n=int(input("Enter a number : "))
# table =[n*i for i in range(1,11)]
# print(table)

# write a program to display a/b where a and b are integers. if b=0,display infinte by handling the 'ZeroDivisionError"
# try:
#     a=int(input("Enter a number: "))
#     b=int(input("Enter second number: "))
#     print(a/b)
# except ZeroDivisionError as v:
#     print("Infinite")

# Stores the multiplication table generated in problem 3 in a file named Tables.txt.
n=int(input("Enter a number : "))
table =[n*i for i in range(1,11)]
with open("Tables.txt","a")as f:
    f.write(f"Table of {n} : {str(table)} \n")
        