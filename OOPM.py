# example of make the class 
# class Employee:
#     language="py"                     This is a class attribute 
#     salary=500000
    
# Rahul =Employee()                   This is an instamce attribute
# print(Rahul.name,Rahul.language)    
# here name is instance attribute and salary & language are class attributes as they directly belong to the class

# Self method is used to refer to the current instance of the class and it is used to access variables that belongs to the class
# class Employee:
#     language="py"                   
#     salary=500000
#     def getInfo(self):
#         print(f"The language is {self.language} and the salary is {self.salary}")
    
# Rahul =Employee()  
# Rahul.getInfo()
# Employee.getInfo(Rahul)       this is also a way to call the method but it is not recommended as it is not oopm way of calling the method


# _Init_() Constructor             it is a special method which is first run as soon as the object is created .
# class Employee:
#     language="py"                     
#     salary=500000
    
#     def __init__(self,name ,salary):                  # dunder method which is automatically called
#         self.name=name
#         self.salary=salary
#         print("I am creating an object")

# Rahul =Employee("Rahul", 60000)                   
# print(Rahul.name,Rahul.language)


#  Practice Question
# class Programmer:
#     company="Microsoft"
#     def __init__ (self,name,salary,pin):
#        self.name=name
#        self.salary=salary
#        self.pin= pin
# p=Programmer("Rahul",120000,45678)  
# print(p.name,p.salary,p.pin,p.company)
# r=Programmer("rohan",120000,45678)  
# print(r.name,r.salary,r.pin,r.company)     


# class Calculator:
#     def __init__(self,n):
#         self.n=n
#     def square(self):
#         return self.n *self.n
#     def cube(self):
#         return self.n *self.n *self.n
#     def Squareroot(self):
#         return self.n ** 0.5

# a=Calculator(4)   
# print(a.square())         
# print(a.cube())         
# print(a.Squareroot())


# class Demo:
#     a=4
# o=Demo()
# print(o.a)     #print the class attribute because instance att is not present
# o.a= 0             #instance attribute is set
# print(o.a)      #print the instance attribute because instance att is not present
# print(Demo.a)        #print the class attribute    


# Adding a static method
# class Calculator:
#     def __init__(self,n):
#         self.n=n
#     def square(self):
#         return self.n *self.n
#     def cube(self):
#         return self.n *self.n *self.n
#     def Squareroot(self):
#         return self.n ** 0.5
#     @staticmethod
#     def hello():
#         print("Hello there!")

# a=Calculator(4)   
# print(a.square())         
# print(a.cube())         
# print(a.Squareroot())
# a.hello()


from random import randint, random
class Train:
    def __init__(self,trainNo):
        self.trainNo =trainNo
    def book(self,fro,to):
        print(f"Ticket is booked in train no: {self.trainNo} from{fro} to{to}")
    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")
    def getFare(self,fro,to):
        print(f"Ticket is fare in train no: {self.trainNo} from{fro} to {to} is {randint(189,555)}")

t=Train(12398)
t.book("Rampur","Delhi")
t.getStatus()
t.getFare("Rampur","Delhi")        