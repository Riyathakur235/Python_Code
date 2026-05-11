# Virtual Environment
# Lambda Functions
# square = lambda n: n * n
# print(square(5))

# Join Method
# a =["rohan","sohan","mohan"]
# final = "-".join(a)
# print(final)

# Format Method(Striings)
# a="{0} is a good {1}".format("Rohan","boy")
# print(a)

# Map,Filter & Reduce
list =[1,2,3,4,5]
# square =lambda x: x*x
# sqList = map(square,list)
# print(list(sqList))

# filter function
# def even(n):
#     if(n%2==0):
#         return True
# onlyEven =filter(even,1)
# print(list(onlyEven))

# Reduce
# from functools import reduce
# def sum(a,b):
#     return a+b
# print(reduce(sum,list))


# Practice Questions
#Q2. write a program to input name ,marks and phoneno. of a student and format it using format function like brlow:
# "The name of the student is rohan, his marks are 72 and phone no. is 98897689"
# name=input("Enter name: ")
# marks=int(input("Enter marks: "))
# phone=int(input("Enter phone no.: "))
# s="The name of the student is {}, his marks are {} and phone no. is {}".format(name, marks, phone)
# print(s)


# A list contains the multiplication table of 7.write a program to convert it to vertical string of same numbers.
# table =[str(7*i) for i in range(1,11)]

# s= "\n".join(table)
# print(s)

# write a program to filter a list of numbers which are divisible by 5.
# def divisible5(n):
#     if(n%5==0):
#         return True
#     return False
# a=[4786,564,839,67,80]
# f=list(filter(divisible5,a))
# print(f)

# write a program to find the maximum of the nummbers in a list using the reduce function.
# from functools import reduce
# def maximum (a,b):
#     if(a>b):
#         return a
#     return b

# a=[475,86,354,454,89]
# print(reduce(maximum,a))

# Explore the 'Flask' module and create a web server using Flask & python.
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
app.run()