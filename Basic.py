#------------- Basic -------------
# Python is high level programming language. it is case sensitive language
# it uses interpretor to convert the high level code into machine code.
# Data types --> int, str, float, bool, none
# string can be written inside the 'name' or "name" or ''' name '''
# type() is used to check the type of the variable

# name1 = 'saten'
# name2 = "saten"
# name3 = '''satendra'''
# print(name1, name2, name3)
# print(type(name1))




#---------- operator -------------
# when we divide the two number in python the answer will the float value irrespective the type of the two numbers
# (a**b) will give the power of a raise to b. This concept is not there in c++.
# logical operator are  --> (and / or / not)
# Non zero number is true

# num1 = 0
# num2 = 20

# if(num1 > 4 and num2 > 100):
#     print("true")
# else:
#     print("False")

# print(not num1)

# print(num1/ num2)
# print(num1 ** num2)



#------------- Type Conversion ---------
# There are two things, one is type conversion and other is typeCasting.
# Type conversion is done by interpretor automatically when we are performing operation in different data type then interpretor convert it into 
# higher data type.
# Type casting is used to convert one type to other forcefully.

# price1 = "134"
# price2 = 134
# sum = int(price1) + float(price2)
# price3 = int(12.4939933)
# print(price3)
# print(sum)



#-------------User input-------------
# input() function is used to take the input from the user from the keyboard
# input function always take the input in the string format i.e the data type of the value taken by it is string.
# so it become necessary to type cast the input depending upon the type of the input that we are taking.

# age = input("Enter the age: ")
# print(type(age))
# print(age)

# price = float(input("Enter the price: "))
# print(price)

username = input("Enter the username: ")
id = int(input("Enter the id: "))
price = float(input("Ente the price: "))
print("username is ", username ,"id is", id,  "and price of the product is ", price)
