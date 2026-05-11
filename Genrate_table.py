
# def genrateTable(n):
#     table=""
#     for i in range(1,11):
#         table+= f"{n} x {i} ={n*i}\n"
#     with open(f"tables/table_{n}","w") as f:
#         f.write(table)

# for i in range(2,21):
#     genrateTable(i)

# replace the donkey word from ###
# word="donkey"
# with open ("file.txt") as f:
#     content=f.read()
# contentNew = content.replace(word,"#####")    
# with open ("file.txt","w") as f:
#     f.write(contentNew)


# change in list 
# words=["donkey","bad","gadha"]
# with open ("file.txt") as f:
#     content=f.read()
    
# for word in words:    
#   content = content.replace(words,"#"*len(word))    
# with open ("file.txt","w") as f:
#     f.write(content)


# in any log python present or not
# with open("log.txt") as f:
#   content=  f.read()
  
# if("python" in content):
#    print("Yes,python is present")   
# else:
#     print("No,python is not present") 


# check python word present in which line
# with open("log.txt") as f:
#   lines=  f.readlines()

# lineno=1  
# for line in lines:
#   if("python" in line):
#      print(f"Yes,python is present. line no.{lineno}") 
#      break
#   lineno+=1  
  
# else:
#     print("No,python is not present") 


# make the copy of file
# with open("this.txt") as f:
#     content=f.read()
    
# with open("this_copy.txt","w") as f:
#      f.write(content)


# check  the file content match or not
# with open("file1.txt") as f:
#    content1=f.read()
   
# with open("text2.txt") as f:
#    content2=f.read()   
# if(content1==content2):
#      print("yes,these files are identical")   
# else:
#     print("No, these files are not identical") 


# wiped out the file content
# with open("text2.txt","w") as f:
#   f.write("")


# rename a file Name
# with open("old.txt") as f:
#     content=f.read()
# with open("this_copy.txt") as f:
#     f.write(content)    