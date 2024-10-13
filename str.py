#----------string--------------
# string in python is same as string in c and c++.
# string are immutable in python i.e we can not change the original string.
# we can represent the string in different way like " " or '' or """ """.
# indexing is given to each of the charector of the string.particular index can not be changed by accesing it's index.
# Negitive indexing is given to the string in python which is start from the - n --> -1 in case of slicing only


# fname = "satendra"
# lname = "yadav"
# middle = "parshuram"
# print(fname + middle +  lname)
# print(len(middle))


#--------- Method in string ----------

# str.endswith("string")
# str.replace("old", "name") 
# str.find("string")  --> return the first occurence of the string from the left
# str.capitalize() --> capitalize the first charactor of the string
# str.count("ab") --> return the occurence of the ab in str
# (str1 + str2) -->  it will concatinate the str1 and str2
# len(str) -->  it will give the length of the string str

# str[startidx: endidx] --> endidx is excluded. if we not specify the first idex then it will take 0 as first and if we not specify
# the last one then it will take the length of the string.it will not change the original string.


# username = "satendra123"
# print(username[1:5])
# print(username[:5])
# print(username[3:])
# print(username[-5: -1])
# print(username)

# fullname = "satendra parshuram Yadav"
# print(fullname.endswith("Yadav"))
# print(fullname.replace("Yadav", "singh"))
# print(fullname.find("Yad"))   
# print(fullname.capitalize())
# print(fullname.count("a"))


# ------ conditional statment ------
# if(): elif(): elif(): else:

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of the b: "))
c = int(input("Enter the value of the c: "))

if(a >= b and a >= c):
    print("A is the greatest number")
    print("The value of a is ", a)
elif(b >= a and b >= c):
    print("B is the greatest number")
    print("The value of the b is", b)
else:
    print("c is the gretest number ")
    print("The value of the c is ", c)





