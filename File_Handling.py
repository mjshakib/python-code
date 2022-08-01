from ast import walk
from fileinput import filename
from importlib.metadata import files
from logging import root
import os
user = ""
while user not  in ["Yes", "No"]:
    user= input("whats u want? read and write say yes or no: ")

    if user.lower() == "yes":
        a = ""
        while a not in [1 ,2]:
        
                a = input("press 1 for file read and press 2 for file write:")
                if a == "1":
                    for root, dirs, files in os.walk(r"C:\Users\shaki\OneDrive\Desktop\read write permission"):
                        file = input("filename: ")
                        # extension = input('Extension: ')
                        # filename = ('{0}.{1}'.format(file, extension))

                        if filename in files:
                             file = open('{0}'.format(filename), "r")
                             b=file.read()
                             print(b)
                             file.close
                        else:
                             print('file not found')
                             print (os.path.join(root))
                        break
                        

                            
                if a == "2":
                    name = input ("name: ")
                    age = input ("age: ")
                    # file= input ("filename: ")
                    file= input('Filename: ')
                    # extension=input('Extension: ')
                    # filename=('{0}.{1}'.format(file,extension))
                    file=open('{0}'.format(filename),"w")
                    a=file.write(' name= {0} \n age ={1} \n file= {2} \n '.format(name, age))
                    print(a)
                    file.close  
                                  
                            

    if user=='no':
            print('sorry')
    break

# import os
# path = ("Enter the path: ")
# os.dirs(path)
# user_input = (" Enter the file for read: ")
# a= user_input + ".txt"  
# if os.path.exists(a):
#   f = open(a,'r')
#   c = f.read()
#   print(c)
#   f.close()
# else:
#   print("file dose't exist")




# def ab  ():
#     bc = "nothing"
    
#     while bc not in ["0","1","2"]:
#         bc = input("Write only (0,1,2):")
        
#         if bc not in ["0","1","2"]:
#             print("this is out of range")
            
#     return int(bc)


# def user_choice ():
#     choice='WRONG'
    
#     while choice.isdigit()==False:
        
#         choice= input("please enter a number (0-10):")
#     return int(choice)


# def user_choice ():
#     choice='WRONG'
    
#     while choice.isdigit()==False:
        
#         choice= input("please enter your name : ")
#     return (choice)


# import ayat

# with open ('ayat.txt',mode='r') as f:
#     print(f.read())
#     f.close()

# file = open("ayat.txt", "w")
# file.write("First Line of Code \n")
# file.close()

# while True:
#         name=input("Enter your name : ") 
        
#         print(open('ayat.txt', mode ='r', encoding= 'cp1252'))

#         if name == int:
#             print("Please Enter Your Name  Not Your Age")
#         else:
#             print(name)
            
#         if name == str:
#             print( open ('ayat.txt',mode='r'))
#         else:
#             print (file = open("ayat.txt", "w"))

# newFile = open("ayat.txt", "w")
# newFile.write("This is how you write to file.")
# newFile.write("And you can add to it. ")
# newFile.write("\n use this for a new file. ")
# newFile.close()
# newFile = open("ayat.txt", "w")
# newFile.write("This will overwrite your file!!")
# newFile.close()


# def user_choice():
    
#     choice= "wrong"
#     acceptable_range= range(10,50)
#     within_range = False
    
#     while choice.isdigit() == False or within_range == False:
        
#         choice = input("Enter your name: ")
        
        
        
#         if choice.isdigit()== False:
#             with open ('newfile.txt',mode='r') as f:
#                 print(f.read())
#             f.close()
            
            
#         input("Enter your name: ")   
#         input("Enter your age: ")
#         if input == int:
#             print("you can read and write this file")
                
        
                
            
        
#         if choice.isdigit()== True:
#             if int(choice) in acceptable_range:
#                    within_range= True
#             else:
#                     within_range= False

                 

# with open ('newfile.txt',mode='r') as f:
#     print(f.read())
#     f.close()

# def user_choice():
    
#     choice= "right"
# #     acceptable_range= range(0,10)
#     within_range = False
    
#     while choice.isdigit() == False or within_range == False:
        
#         choice = input("Enter your name: ")
        
        
#         if choice.isdigit()== False:
#             with open ('newfile.txt',mode='r') as f:
#                 print(f.read())
#                 f.close()




# def user_choice():
    
#     choice= "right"
#     acceptable_range= range(0,10)
#     within_range = False
    
#     while choice.isdigit() == False or within_range == False:
        
#         choice = input("Enter your name: ")
        
        
#         if choice.isdigit()== False:
#             with open ('newfile.txt',mode='r') as f:
#                 print(f.read())
#                 f.close()
                
#         name = input("Enter your name:")
#         age = input("Enter your age")
#         if choice.isdigit() == True:
#             with open ('newfile.txt',mode='w') as f:
#                 print(f.write())
#                 f.close()

            
    



