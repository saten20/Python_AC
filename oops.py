#----------------OOP's---------------------

# initally there is procedural oriented programming and the functional oriented. Now we have object oriented programming.
# class is the blue print and object is the actual things.
# first letter of the class name should be capital.
# obj = Classname() --> this is how we create the object in python
# we have to pass the self arguments inside the function of the class, so that we can access the attributes.




# class Student:
#     college = "NITK Surthkal"    # class member
#     def __init__(self, name, rollno):
#         self.name = name   # object member
#         self.rollno = rollno
#     def printData(self):
#         print(self.name, self.rollno, self.college)
# s = Student("satendra", 124)
# s.printData()




#-----------------constructor------------

# def __init__(self) is the constrctor of the class. 
# self contain the address of the calling object.
# There are two type of the constrctor. default and parameterized. default constructor is call by the interpretor automatically.
# self.name,  self will represent that we are refering the name variable of class.


# class Student:
    
#     def __init__(self):
#         pass
#     def __init__(self, name, rollno):
#         self.name = name
#         self.rollno = rollno
    

# s =  Student("satendra", 123)
# print(s.name)
# print(s.rollno)





#-------------------@staticmethod & @classmethod--------------------

# class / static  member will be created even without creating object.
# To create the statice member function we have to use the decorator i.e @staticmethod, and for class @classmethod
# @staticmethod does not access the member of the class. it is used to do the static task only.
# @classmethod will access the members of the class and perform the changes in the members accordinly.
# instance method access the members of the instance and have self in it.
# Decorator is a function which take the function as an argument and convert it into static member function and return the function.
# To call the class members we can use classname.name/classname.show() or normally with object name.



# class Student:
#     college = "NITK surthkal"

#     def __init__(self):
#         pass

#     def __init__(self,name, rollno):
#         self.name = name
#         self.rollno = rollno


# s1 = Student("saten",23)
# print(s1.name," ",s1.rollno," ", Student.college)
# print(s1.college)


# class Details:
#     list = []
#     def __init__(self, name, list):
#         self.name = name
#         self.list.append(list[0])
#         self.list.append(list[1])
#         self.list.append(list[2])
    
#     @staticmethod   #decorator
    
#     def welcome():
#         print("Hello student, welcome to NITK")
    
#     def avg(self):
#         print("Average marks of ",self.name)
#         return (self.list[0] + self.list[1] + self.list[2]) / 3

# marks = [40,49,40]
# d = Details("satendra",marks)
# Details.welcome()
# print(" is ", d.avg())


# class Student:
#     name = "satendra"

#     @staticmethod
#     def show():
#         print("hello")


#     @classmethod
#     def change(cls):
#         print(cls)
#         cls.name = "jatin"
#         print(Student.name)

# s = Student()
# Student.change()
    


#-----------------access specifier and delete ----------------

# del objname -> it will delete the object
# By default all the member function and member varibale of the class are public.
# To make them private we use __function or __variable.that is we use underscor just before the variable name or function name

# class Display:
#     __name = "satendra"
#     def __init__(self):
#         pass
    
#     def __show(self):
#         print("This is the private method")
    
#     def callme(self):
#         self.__show()
#         print("private method call by using the public method")

# d = Display()
# # print(d.name)
# del d
# d.callme()


#---------------- @property  decorator ----------------

# when we want to define the function as a property(variable) then we will use the property decorator.
# Suppose if we defind any property inside the constructor then as we know construtor will run only once. but if any changes made in the
# values then it will not change the property value.
# This can solve by using the function also. but instead of that we can use the @property decorator.


class Student:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    
    @property
    def per(self):
        return str((self.a + self.b + self.c) / 3)

obj = Student(89,89,89)
print(obj.per)              # function as a varibale or attribute
obj.c = 100
print(obj.per)
