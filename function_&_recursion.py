# Function Defination
# def avg():
#     a=int(input("Enter the number: "))
#     b=int(input("Enter the number: "))
#     c=int(input("Enter the number: "))
    
#     average=(a+b+c)/3
#     print(average)
    
# avg()                   #  function call

# Function with argument
# def goodDay(name):
#     print("Good Day, " +name)
    
# goodDay("Rohan")    
    
    
# Recusion Question
# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n* factorial(n-1)
# n=int(input("Enter a number: "))
# print(f"The factorial of this number is: {factorial(n)}")


# find greatest of three number
# def greatest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     else:
#         return c
# print(greatest(2,5,7))   

#  celcius to frenhide
# def f_to_c(f):
#     return 5*(f-32)/9
# f=int(input("Enter temprature: "))
# print(f"{round(f_to_c(f),2)} ")


# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1) +n

# print(sum(4))


# def pattern(n):
#     if(n==0):
#      return
#     print("*"*n)
#     pattern(n-1)
# pattern(3)   


# remove word and strip at the same time
def rem(l,word):
    n=[]
    for item in l:
        # l.remove(word)
        # return l
        if not(item == word):
            n.append(item.strip(word))
    return n        
l=["Hariram","Rohan","Shubham","an"]
print(rem(l,"an"))


# Multiplication table
# def table(n):
#     for i in range(1,11):
#         print(f"{n} x {i} = {n*i}")
        
# table(8)        
