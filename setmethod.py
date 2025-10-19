# s={12,34.5,"Python",True,1,3,35,12}      
# print(s)
# in given set 1 is consider as boolen value is 1 is not print

# s={12,34.5,"Python",True,1,3,35,12}
# print(s)
# print(s[0])
# s[0]=123
# error - Because in the set sequence is alwase change so index is not working.

# s={12,34.5,"Python",True,1,3,35,12}
# print(s)
# s.add(120)
# print(s)
 
#  s.add(100,200,300)
# error it can only add one element not many.

# s={12,34.5,"Python",True,1,3,35,12}
# print(s)
# t=(100,200,300)
# s.add(t)
# print(s)
# by using tuple we can the multiple element but they can't add properly , they get add with bracket.it consider that it is a one string.

# s={12,34.5,"Python",True,1,3,35,12}
# print(s)
# t={100,200,300)}        
# s.add(t)
# print(s)
#error    -  tuple can add in set . But set , list , dictionry cannot add in the set.

# In update method it add the string single single element

# s={12,34.5,"Python",True,1,3,35,12}
# print(s)
# s.update("hello")
# print(s)

# s={12,34.5,"Python",True,1,3,35,12}
# print(s)
# s.update("hello",1,2,3)
# print(s)
#  error

# s={12,34.5,"Python",True,1,3,35,12}
# print(s)
#s.update("hello","good","world")
# print(s)
# it also add single single element

# s={12,34.5,"Python",True,1,3,35,12}
# print(s)
# t=("hello","good","world",20,30)
# s.update(t)
# print(s)

# In update by using tuple it get add properly.
# In update set , list ,dictinory work .but in dictinory only key vaule is add.

# s={12,34.5,"Python",True,1,3,35,12}
# print(s)
# t={"key":"value"}
# s.update(t)
# print(s)

# copy method

# s={12,34.5,"Python",True,1,3,35,12}
# print(s)
# s1=s.copy()
# print(s1)

# in pop method it remove first method

# s={12,34.5,"Python",True,1,3,35,12}
# print(s)
# s.pop()
# print(s)

# Remove method it remove the perticular string or number.

# s={12,34.5,"Python",True,1,3,35,12}
# print(s)
# s.remove("Python")
# print(s)

# In python code is execute line by line.
# If error comes next line does not execuete.
#  Discard method also work as remove but given srting is not present it does not show error it excute next line .
# s={12,34.5,"Python",True,1,3,35,12}
# print(s)
# s.discard("python")
# print(s)
# print("Hello world....")

# Clear method remove all the element in the set .

# s={12,34.5,"Python",True,1,3,35,12}
# print(s)
# s.clear()
# print(s)

# String get converted into set 

# s="Hello world"
# print(set(s))

#error
# s=23
# print(set(s)) 

# List get convetrd into set .

# s=[1,2,3,4]
# print(set(s)) 

# tuple also get conveted into set

# s=(1,2,3,4)
# print(set(s)) 

# Dictinonary also get add but only key .

# s= {"key":"value","name":"john"}
# print(set(s))

# Intersection mean common element in both set .

# s={10,20,30,4,5,6}
# s1={1,2,30,4,7,8}
# result=s.intersection(s1)
# print(result)

# Union mean combine both the set but not repeat the value .

# s={10,20,30,4,5,6}
# s1={1,2,30,4,7,8}
# result=s.union(s1)
# print(result)

# Symmetric difference mean commen things are not written .

# s={10,20,30,4,5,6}
# s1={1,2,30,4,7,8}
# result=s.symmetric_difference(s1)
# print(result)


# Difference method  from s it cannot take commen things

# s={10,20,30,4,5,6}
# s1={1,2,30,4,7,8}
# result=s.difference(s1)
# print(result)

# subset mean it check a element is in b 

# a={"a","b","c"}
# b={"f","e","a","d","b","c"}
# result=a.issubset(b)
# print(result)

#  Membership operator 

# b={"f","e","a","d","b","c"}
# print("f" in b)

# b={"f","e","a","d","b","c"}
# print("f" not in b)