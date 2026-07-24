# marks ={
#     "harry": 99,
#     "shubham":76,
#     "rohan": 56
# }

# d={}   empty dict

# print(marks,type(marks))
# print(marks["harry"])

# Metods in dictonary
# print(marks.items())

# print(marks.keys())

# marks.update({"harry":94 , "rehan": 98})
# print(marks)

# print(marks.get("harry"))     prints none
# print(marks["harry"])        gives error if key is not present

# Sets
# s={1,2,5,5,8}         #repetative values are not allowed in set, it will only take unique values
# e=set()     don't use s={} as it will create an empty dictonary, this create an empty set

# s.add(566)
# print(s,type(s))

# sets union and intersection
s1={1,2,3,4}
s2={3,4,5,6}
print(s1.union(s2))
print(s1.intersection(s2))

# Practice Question
# words = {
#     "madad" :"help" ,
#     "kursi" :"chair" ,
#     "billi" :"cat",
# }

# word = input("enter the word you want meaning of: ")
# print(words[word])


s=set()
n= input("Enter number : ")
s.add(int(n))
n= input("Enter number : ")
s.add(int(n))
n= input("Enter number : ")
s.add(int(n))
n= input("Enter number : ")
s.add(int(n))
n= input("Enter number : ")
s.add(int(n))

# print(s)

# s=set()
# s.add(18)
# s.add("18")
# print(s)

# d={}
# name= input("Enter friend name: ")
# lang = input("Enter language name: ")
# d.update({name: lang})

# name= input("Enter friend name: ")
# lang = input("Enter language name: ")
# d.update({name: lang})

# name= input("Enter friend name: ")
# lang = input("Enter language name: ")
# d.update({name: lang})
# print(d)

# s={8,7,12,"Harry",[1,2]}           sets cannot define list as it is mutable.

