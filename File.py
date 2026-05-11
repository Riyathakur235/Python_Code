# using with statement to open a file
# f=open("file.txt")
# data =f.read()
# print(data)
# f.close()


# writing to a file
# st ="hey there,how are you doing?"
# f=open("file.txt","w")
# f.write(st)
# f.close()

# f=open("file.txt")
# It will read whole file and return as list of lines
# lines=f.readlines()
# print(lines,type(lines))

# it will read one line at a time and return as string
# line1 =f.readline() 
# print(line1,type(line1))
# f.close()

# print all lines one by one
# f=open("file.txt")
# line =f.readline()
# while(line!=""):
#     print(line)
#     line=f.readline()
# f.close()    

# in this we don't have to close the file as it will automatically close
# with open("file.txt") as f:
#     print(f.read())


# practice questions
# f=open("poem.txt")
# content=f.read()
# if("twinkle" in content):
#     print("twinkle is present in the poem")
# else:
#     print("twinkle is not present in the poem")
# f.close()

# play the game and update the hiscore
# import random
# def game():
#     print("You are playing the game...")
#     score = random.randint(1,62)
#     # fetch the hiscore
#     with open("hiscore.txt") as f:
#         hiscore= f.read()
#         if(hiscore==""):
#             hiscore =int(hiscore)
#         else:
#             hiscore=0   
             
#     print(f"Your score: {score}")
#     if(score>hiscore or hiscore==""):
#         # write this hiscore to the file
#          with open("hiscore.txt","w") as f:
#             f.write(str(score))
#     return score

# game()


