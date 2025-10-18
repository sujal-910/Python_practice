# s = "Python is easy"
# print(s)
# print(type(s))
# print(len(s))

# Indexing is of two type 
#  +ve index start from 0 ,it work from left to right 
#  -ve index start from -1 ,it work from right to left 

# s = "Python is easy"
# print(s)
# print(s[0])

# s = "Python is easy"
# print(s)
# print(s[3])

# s = "Python is easy"
# print(s)
# print(s[-3])

#  Slicing 
# [Start : End : Step]
#  In slicing the end is taken of previous of string.

# s = "Python is easy"
# print(s)
# print(s[1:4])

# s = "Python is easy"
# print(s)
# print(s[1:4:2])

# s = "Python is easy"
# print(s)
# print(len(s))
# print(s[100])     
# ..- Error index out of range

# s = "Python is easy"
# print(s[0:100])

# print(s[250:100])      
# ..- It consider empty space

# print(s[:100])        
# ..-  When we not mention start or end it consider 0 .

# print(s[:])

# print(s[::2])

# print(s[::-1])      
# ....- When we give -1 then string is print reverse

# print(s[-1:-4]) 
# .....-  Index should start from left to right only

# print(s[-4:-1])

# s = "Python is easy"
# print(s)
# print(s+1)    
# ..- Error we can combine only string not integer

# s = "Python is easy"
# print(s)
# print(s +  "1")

# s = "Python is easy"
# p="Good evening"
# print(s + " " + p)

# s = "Python is easy"
# print(s - 1)    
# ..- Error unsupported operand 

# s = "Python is easy"
# print(s*4)     
# ..- print the string multiple time (4) time 

# s="          Python        "
# print(s)
# print(len(s))

# s="          Python        "
# print(s)
# result=s.lstrip()    
# print(result)
# .. -- in lstrip it remove the blank from left side

# s="          Python        "
# print(s)
# result=s.rstrip()
# print(len(result))    
# print(result)
# .. -- In rstrip it remove the blank space from the right side

# s="          Python        "
# print(s)
# result=s.strip()       
# print(result)
# .. -- In strip method it remove blank space from the both side

# s = input("Enter any number")
# print(s)

# s = input("Enter any number : ")
# print(s+1)      
#  .... -- can only combine string not integer


# s = input("Enter any number")
# print(s)
# int(s)
# print(type(s))

# s = int(input("Enter any number : "))
# print(s)
# print(type(s))

# s = int(input("Enter any number : "))
# print(s+1)
# print(type(s))

# s = float(input("Enter any number : "))
# print(s)
# print(type(s))

# s = list(input("Enter any number : "))
# print(s)

# print(type(s))
  

## This work on list , tuple , set but not in dictionary . not work in dictionary because it has key and value format.

# s="Findatapythondata"
# result=s.find("ata")    
# print(result)
# .. -- find method show the index .

# s="Findatapythondata"
# result=s.count("ata")    
# print(result)
# .. - Count method count how many time string is come. if specific string is not present then it provide -1.

# s = "Python data python data"
# print(s)
# result=s.split(" ")     
# print(result)
# .. split mean divide . in python and data there is space so we provide space in double inverted comma then it undestand that it has to sperate in space.


# s =s = "Python is Hard "
# print(s)
# result=s.replace("Hard","Easy")
# print(result)

# s = "Python is Hard Python is Hard Python is Hard"
# print(s)
# result=s.replace("Hard","Easy")
# print(result)

# s = "Python is Hard Python is Hard Python is Hard"
# print(s)
# result=s.replace("Hard","Easy",1)     
# print(result)
# ... - in this it change only first valus


# s = "Python is Hard Python is Hard Python is Hard"
# print(s)
# new=input("Enter text to replace : ")
# result=s.replace("Hard",new,2)
# print(result)

# c=("c++","Python","Hello")
# print(c)
# result=" ".join(c)
# print(result)

# c=("c++","Python","Hello")
# print(c)
# result="*".join(c)
# print(result)


# s="Python"
# print(s)
# result=s.lower()    
# print(result)
# ... - it make over all string small letters


#   it make all the given string in capital letters
# s="Python"
# print(s)
# result=s.upper()     
# print(result)

# In the title method every letter first word become capital

# s="python python is easy"
# print(s)
# result=s.title()      
# print(result)

# In the capitaliz method first word first letter become capital

# s="python is easy"
# print(s)
# result=s.capitalize()
# print(result)

# In swapcase upper case letter get conver into lowercase and lowecase become uppercase
# s="PythOn is Easy"
# print(s)
# result=s.swapcase()
# print(result)

# in center method perticular string go to the center and we have to provide what should be in blank space

# s="Python"
# print(s)
# print(len(s))
# result=s.center(20," ")
# print(result)
# print(len(result))

# s="Python"
# print(s)
# print(len(s))
# result=s.center(20,"*")
# print(result)
# print(len(result))

# isalnum mean alphbet and number its output come in true or false
# s="Python"
# print(s)
# result=s.isalnum()
# print(result)

# s="1234"
# print(s)
# result=s.isalnum()
# print(result)

# s.isalpha mean given string is alphbet

# s="Python"
# print(s)
# result=s.isalpha()
# print(result)
 
# isdigit mean number

# s="1234"
# print(s)
# result=s.isdigit()
# print(result)

# It check given string is in uppercase or not

# s="Python"
# print(s)
# result=s.isupper()
# print(result)

# it check string is in lower case or not

# s="Python"
# print(s)
# result=s.islower()
# print(result)


# s="Python"
# print(s)
# result=s.istitle()
# print(result)

# it check the space . but empty sting is only consider as space .

# s="Python is easy"
# print(s)
# result=s.isspace()
# print(result)

# menbership operator

# s="Python"
# print(s)
# result=("n" in s)
# print(result)

# s="Python"
# print(s)
# result=("n"  not in s)
# print(result)

# startswitch mean given string is start form that letter . and output come in true or false

# s="Python is dynamic language"
# print(s)
# result=(s.startswith("P"))
# print(result)

#endswith mean given string is end with that letter

# s="Python"
# print(s)
# result=(s.endswith("n"))
# print(result)
