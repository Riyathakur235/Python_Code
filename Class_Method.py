# class Employee:
#     a=1
#     @classmethod
#     def show(cls):
#         print(f"The class value of a is {cls.a}")
        
# e=Employee()
# e.a=45
# e.show()


# Property Decorators
# class Employee:
#     a=1
#     @classmethod
#     def show(cls):
#         print(f"The class value of a is {cls.a}")
    
#     @property
#     def name(self):
#         return f"{self.fname} {self.lname}"
    
#     @name.setter
#     def name (self,value):
#        self.fname =value.split(" ")[0]
#        self.lname =value.split(" ")[1] 
       
# e=Employee()
# e.a=45
# e.name ="Harry yadav"
# print(e.fname,e.lname)
# e.show()


# Operator Overloading
# class Number:
#      def __init__(self,n):
#        self.n = n   
#      def __add__(self,num):
#        return self.n + num.n    
# n=Number(1)
# m=Number(2)
# print(n+m)  


#Practice  Question
# class TwoDVector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j =j 
#     def show(self):
#         print(f"the vector is {self.i}i + {self.j}j ")
# class ThreeDVector(TwoDVector):
#     def __init__(self,i,j,k):
#        super().__init__(i,j)
#        self.k =k      
#     def show(self):
#         print(f"the vector is {self.i}i + {self.j}j + {self.k}k")
       
# a=TwoDVector(1,2)
# a.show()
# b=ThreeDVector(1,2,3)           
# b.show()


# class Animals:
#   pass
# class Pets(Animals):
#      pass
# class Dog(Pets) : 
#     @staticmethod
#     def bark():
#       print("Bow Bow!")  
      
# d=Dog()      
# d.bark()

# class Employee:
#     salary =234
#     increment =20
#     @property
#     def salaryAfterIncrement(self):
#         return (self.salary +self.salary *(self.increment/100) )
    
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self,salary):
#        self.increment= ((salary/self.salary)-1)*100
        
# e=Employee()
# # print(e.salaryAfterIncrement)
# e.salaryAfterIncrement = 280.8
# print(e.increment)

# class Complex:
#     def __init__(self,r,i):
#         self.r =r
#         self.i=i
#     def __add__(self,c2):
#         return Complex(self.r + c2.r ,self.i +c2.i) 
#     def __str__(self):
#        return f"{self.r} +{self.i}i"    

# c1 =Complex(1,2)
# c2=Complex(3,4)    
# print(c1+c2)


class Vector:
    def __init__(self,x,y,z):
        self.x =x
        self.y=y
        self.z=z
    def __add__(self, other):
        result =Vector(self.x+ other.x, self.y+other.y, self.z+other.z)
        return result
    
    def __mul__(self,other):
        result =self.x* other.x+ self.y*other.y+ self.z*other.z
        return result
    def __str__(self):
        return f"Vector({self.x}, {self.y},{self.z})"    
    
v1=Vector(1,2,3)
v2=Vector(4,5,6)
v3=Vector(7,8,9)
print(v1+v2)
print(v1*v2)  
print(v1+v3)
print(v1*v3)  